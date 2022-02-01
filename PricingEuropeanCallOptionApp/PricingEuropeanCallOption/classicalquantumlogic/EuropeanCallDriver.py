from qiskit.algorithms import IterativeAmplitudeEstimation, EstimationProblem

from classicalquantumlogic.EuropeanCallQuantumRequest import EuropeanCallQuantumRequest
from classicalquantumlogic.EuropeanCallEstimation import EuropeanCallEstimation
from quantumlogic.algorithms.QuantumAmplitudeEstimationAlgorithm import QuantumAmplitudeEstimationAlgorithm

class EuropeanCallDriver:

    def __init__(self, problem, objective):
        self.quantumRequest = EuropeanCallQuantumRequest()
        self.QAEAlgorithm = QuantumAmplitudeEstimationAlgorithm(problem, objective)
        
    
    def setQuantumRequestParameters(self, epsilon, alpha, shots):
        self.quantumRequest.setParameters(epsilon, alpha, shots)

   
    def estimateEuropeanCall(self):
        self.estimationProblem = EstimationProblem(
            state_preparation=self.QAEAlgorithm.getEuropeanCallQuantumCricuit(),
            objective_qubits=[3],
            post_processing=self.QAEAlgorithm.getObjective().getLinearAmplitudeFunction().post_processing,
        )
        # construct amplitude estimation
        self.iterativeAmplitudeEstimation = IterativeAmplitudeEstimation(self.quantumRequest.epsilon, alpha=self.quantumRequest.alpha, quantum_instance=self.quantumRequest.getQuantumInstance())
        
        self.result = self.iterativeAmplitudeEstimation.estimate(self.estimationProblem)
        
        return EuropeanCallEstimation(self.result)
    
    
    def getQAEAlgorithm(self):
        return self.QAEAlgorithm
    
        
        
        
        
        
        
        
        