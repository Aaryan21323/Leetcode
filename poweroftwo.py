# solution using function not optimal need to consider many edge cases
import math
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n<=0:
            return False
        x=int(math.log(n,2))

        if (2**x)==n:
            return True
        else:
            return False


# optimal solution using bit manipulation
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and (n & (n - 1)) == 0
    
"""
n & (n - 1) == 0 bit manipualtion

8     = 1000
8 - 1 = 0111
--------------
&     = 0000
"""