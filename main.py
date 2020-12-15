import numpy as np

def compute_b( spins ) :
  b = 0
  # Your code goes here
  for i in range(len(spins)) : 
      if spins[i]==1 : b = b + 2**i 
  return b
  
print( compute_b([1,1,1]) )
print( compute_b([-1,1,1]) )
print( compute_b([1,-1,1]) )
print( compute_b([-1,-1,1]) )
print( compute_b([1,1,-1]) )
print( compute_b([-1,1,-1]) )
print( compute_b([1,-1,-1]) )
print( compute_b([-1,-1,-1]) )
