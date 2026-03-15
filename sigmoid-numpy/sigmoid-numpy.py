import numpy as np

def sigmoid(x):
    """
    Vectorized sigmoid function.
    """
    x =  np.asarray(x, dtype=float)

    result = 1 / (1 + np.exp(-x))
    
    # Return scalar if input was scalar
    if result.size == 1:
        return float(result)
    
    return result
    pass