from businesslogic.entities.EuropeanCallProblem import EuropeanCallProblem
from businesslogic.entities.EuropeanCallObjective import EuropeanCallObjective
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import time

class EuropeanCallController:
    
    def __init__(self):
        self.problem = None
        self.objective = None
        self.plotPath = None
        return

    def createProblem(self, spotPrice, volatility, anualRate, maturityDays):
        self.problem = EuropeanCallProblem(spotPrice, volatility, anualRate, maturityDays)
    

    def getProblemPlot(self):
        # plot probability distribution
        plt.cla()
        if self.getProblem() is not None:
            x = self.getProblem().getUncertaintyModel().values
            y = self.getProblem().getUncertaintyModel().probabilities
            plt.bar(x, y, width=0.15)
            plt.xticks(x, size=15, rotation=90)
            plt.yticks(size=15)
            plt.grid()
            plt.xlabel("Spot Price at Maturity $S_T$ (\$)", size=15)
            plt.ylabel("Probability ($\%$)", size=15)
            #plt.show()
            self.plotPath = 'static/UncertaintyModel_'+str(time.time())+'.png'
            figure = plt. gcf()
            figure. set_size_inches(9, 9)
            plt.savefig(self.plotPath, dpi=45)
            plt.close('all')
                       
        return self.plotPath
    
 
    def createObjectiveFunction(self, strikePrice, cApprox):
        self.objective = EuropeanCallObjective(float(strikePrice), float(cApprox), self.getProblem().low, self.getProblem().high, self.getProblem().NUM_UNCERTAINTY_QUBITS)
        
        

 
    def getObjectivePlot(self):
        # plot exact payoff function (evaluated on the grid of the uncertainty model)
        plt.cla()
        self.plotPath=None
        if self.getObjective() is not None:
            x = self.getProblem().getUncertaintyModel().values
            y = np.maximum(0, x - self.getObjective().strikePrice)
            plt.plot(x, y, "ro-")
            plt.grid()
            plt.title("Payoff Function", size=15)
            plt.xlabel("Spot Price", size=15)
            plt.ylabel("Payoff", size=15)
            plt.xticks(x, size=15, rotation=90)
            plt.yticks(size=15)
            self.plotPath = 'static/ObjectiveModel_'+str(time.time())+'.png'
            figure = plt. gcf()
            figure.set_size_inches(9, 9)
            plt.savefig(self.plotPath, dpi=45)
            plt.close('all')
            return self.plotPath
        return None
            
    
    
    def getExactExpectedValue(self):
        # evaluate exact expected value (normalized to the [0, 1] interval)
        
        x = self.getProblem().getUncertaintyModel().values
        y = np.maximum(0, x - self.getObjective().strikePrice)
        
        self.exactValue = np.dot(self.getProblem().getUncertaintyModel().probabilities, y)
        print("exact expected value:\t%.4f" % self.exactValue)
        return self.exactValue
    
    
    def getExactDeltaValue(self):
        x = self.getProblem().getUncertaintyModel().values
        self.exactDelta = sum(self.getProblem().getUncertaintyModel().probabilities[x >= self.getObjective().strikePrice])
        print("exact delta value:   \t%.4f" % self.exactDelta)
        return self.exactDelta
    
            
    def getProblem(self):
        return self.problem
    
    def resetProblem(self):
        self.problem=None
    
    def getObjective(self):
        return self.objective