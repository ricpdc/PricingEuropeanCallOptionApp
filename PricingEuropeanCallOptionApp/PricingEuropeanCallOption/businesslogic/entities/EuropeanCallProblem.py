import numpy as np
from qiskit_finance.circuit.library import LogNormalDistribution

class EuropeanCallProblem:
    
    # number of qubits to represent the uncertainty
    NUM_UNCERTAINTY_QUBITS = 3
       
    def __init__(self, spotPrice, volatility, anualRate, maturityDays):
        # parameters for considered random distribution
        self.spotPrice = spotPrice  # initial spot price
        self.volatility = volatility  # volatility of 40%
        self.anualRate = anualRate  # annual interest rate of 4%
        self.maturityTime = maturityDays / 365  # days to maturity
        
        self.createDistribution()
    
    def createDistribution(self):
        # resulting parameters for log-normal distribution
        self.mu = (self.anualRate - 0.5 * self.volatility ** 2) * self.maturityTime + np.log(self.spotPrice)
        self.sigma = self.volatility * np.sqrt(self.maturityTime)
        self.mean = np.exp(self.mu + self.sigma ** 2 / 2)
        self.variance = (np.exp(self.sigma ** 2) - 1) * np.exp(2 * self.mu + self.sigma ** 2)
        self.stddev = np.sqrt(self.variance)
        
        # lowest and highest value considered for the spot price; in between, an equidistant discretization is considered.
        self.low = np.maximum(0, self.mean - 3 * self.stddev)
        self.high = self.mean + 3 * self.stddev
        
        # construct A operator for QAE for the payoff function by composing the uncertainty model and the objective
        self.uncertaintyModel = LogNormalDistribution(self.NUM_UNCERTAINTY_QUBITS, mu=self.mu, sigma=self.sigma ** 2, bounds=(self.low, self.high))
        
        
    def getParams(self):
        return 'Model Params: S={}, vol={}, r={}, T={:.4f}'.format(self.spotPrice, self.volatility, self.anualRate, self.maturityTime)
        
    
    def getUncertaintyModel (self):
        return self.uncertaintyModel
    
  
        
        