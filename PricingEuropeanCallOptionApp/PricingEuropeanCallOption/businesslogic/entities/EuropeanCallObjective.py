from qiskit.circuit.library import LinearAmplitudeFunction

class EuropeanCallObjective:
    
    def __init__(self, strikePrice, cApprox, low, high, numUncertaintyQubits):
        # set the strike price (should be within the low and the high value of the uncertainty)
        self.strikePrice = strikePrice
        # set the approximation scaling for the payoff function
        self.cApprox = cApprox
        
        
        # setup piecewise linear objective function
        self.breakpoints = [low, strikePrice]
        self.slopes = [0, 1]
        self.offsets = [0, 0]
        self.f_min = 0
        self.f_max = high - self.strikePrice
        self.linearAmplitudeFunction = LinearAmplitudeFunction(
            numUncertaintyQubits,
            self.slopes,
            self.offsets,
            domain=(low, high),
            image=(self.f_min, self.f_max),
            breakpoints=self.breakpoints,
            rescaling_factor=self.cApprox,
        )
    
    
    def getLinearAmplitudeFunction(self):
        return self.linearAmplitudeFunction
    
        