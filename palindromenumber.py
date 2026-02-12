class Solution:
    def palindromeNumber(self, x: int) -> bool:
        if x < 0:
            return False
        
        reversed_num = int(str(x)[::-1])
        return x == reversed_num

# pythonic way
class Solution1:
    def palindromeNumber(self, x: int) -> bool:
        return str(x) == str(x)[::-1]

x = 121
sol = Solution()
print(sol.palindromeNumber(x))
