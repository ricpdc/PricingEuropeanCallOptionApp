# Portions of this file are adapted from the Qiskit Finance
# "Pricing European Call Options" tutorial.
#
# Original Qiskit material:
# Copyright 2017 IBM and its contributors.
# Licensed under the Apache License, Version 2.0.
#
# Modified and integrated into PricingEuropeanCallOptionApp by
# Ricardo Pérez-Castillo and contributors.
#
# Modifications include its integration into the architecture of a
# hybrid classical-quantum application and adaptation to the application's
# domain and execution model.
#
# See LICENSE and THIRD_PARTY_NOTICES.md for details.


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
