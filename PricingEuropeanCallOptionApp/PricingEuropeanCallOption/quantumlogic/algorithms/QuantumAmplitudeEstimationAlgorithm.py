from qiskit import QuantumCircuit
import time

class QuantumAmplitudeEstimationAlgorithm:

	def __init__(self, problem, objective):
		# construct A operator for QAE for the payoff function by composing the uncertainty model and the objective
		num_qubits = objective.getLinearAmplitudeFunction().num_qubits
		self.num_qubits = num_qubits
		self.problem = problem
		self.objective = objective
		self.europeanCallQuantumCricuit = QuantumCircuit(num_qubits)
		self.europeanCallQuantumCricuit.append(problem.getUncertaintyModel(), range(problem.NUM_UNCERTAINTY_QUBITS))
		self.europeanCallQuantumCricuit.append(objective.getLinearAmplitudeFunction(), range(num_qubits))
		
		
	def getEuropeanCallQuantumCricuit(self):
		return self.europeanCallQuantumCricuit
	
	
	def getCircuitImage (self):
		# draw the circuit
		self.circuitPath='static/Circuit_'+str(time.time())+'.png'
		self.getEuropeanCallQuantumCricuit().draw(output='mpl', filename=self.circuitPath)
		return self.circuitPath
	
	
	def getProblem(self):
		return self.problem;
	
	def getObjective(self):
		return self.objective