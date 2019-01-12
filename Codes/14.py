# 
# This problem was asked by Google.

# The area of a circle is defined as πr^2. 
# Estimate π to 3 decimal places using a Monte Carlo method.
# 
# 
# 
# 



import numpy as np

def estimatePI(r=1):
    
    x = np.random.random(100000)
    
    y = np.random.random(100000)
    
    
    print(sum([1 for a,b in zip(x,y) if( a**2 + b**2 <= r)])/100000 * 4)
    
estimatePI()
