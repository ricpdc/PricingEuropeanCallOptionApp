from qiskit import Aer
from qiskit.utils import QuantumInstance

class EuropeanCallQuantumRequest:
    
    def __init__(self):
        # set target precision and confidence level    
        self.epsilon = 0.01
        self.alpha = 0.05
        self.shots=100
        self.quantumComputer = Aer.get_backend("aer_simulator")
        self.quantumInstance = QuantumInstance(self.quantumComputer, self.shots)


    def setParameters(self, epsilon, alpha, shots):
        self.epsilon=epsilon
        self.alpha=alpha
        self.shots=shots
        self.quantumInstance = QuantumInstance(self.quantumComputer, self.shots)
        
    
    def getQuantumInstance(self):
        return self.quantumInstance
        
        
        
        
        
        
        
        