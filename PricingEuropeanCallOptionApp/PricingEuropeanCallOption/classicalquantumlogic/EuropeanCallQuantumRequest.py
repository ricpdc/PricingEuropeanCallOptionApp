from qiskit_aer import Aer

from qiskit_ibm_runtime import SamplerV2 as Sampler

class EuropeanCallQuantumRequest:
    
    def __init__(self):
        # set target precision and confidence level    
        self.epsilon = 0.01
        self.alpha = 0.05
        self.shots=100
        self.quantumComputer = Aer.get_backend("aer_simulator")
        self.quantumInstance = Sampler(self.quantumComputer, self.shots)


    def setParameters(self, epsilon, alpha, shots):
        self.epsilon=epsilon
        self.alpha=alpha
        self.shots=shots
        self.quantumInstance = Sampler(self.quantumComputer, self.shots)
        
    
    def getQuantumInstance(self):
        return self.quantumInstance
        
        
        
        
        
        
        
        