import numpy as np

class EuropeanCallEstimation:

    def __init__(self, result):
        self.result=result
        self.confInt = np.array(self.result.confidence_interval_processed)
     
     
    def showResults(self):   
        #print("Exact value:        \t%.4f" % exact_value)
        print("Estimated value:    \t%.4f" % (self.result.estimation_processed))
        print("Confidence interval:\t[%.4f, %.4f]" % tuple(self.confInt))
        
    
    def getEstimatedValue(self):
        return self.result.estimation_processed
    
    def getConfidenceInterval(self):
        return tuple(self.confInt)