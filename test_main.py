import unittest
from main import *

class UnitTests(unittest.TestCase) :
    def test_b_calculation(self) : 
        for k in range(1,6) :
            for i in range(2**k) :
                num, spins = i, k*[0]
                for j in range(k) :
                    spins[k - 1 - j] = np.floor( num / 2**(k-1-j) )
                    num = num - spins[k - 1 - j]*2**(k-1-j)
                    if spins[k-1-j]==0 : spins[k - 1 - j] = -1
                self.assertTrue( compute_b( spins )==i, "the function for calculating b does not return the correct value" )
