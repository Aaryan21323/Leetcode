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
    
# Another Way pointer way

class Solution2:
    def palindromeNumber(self,x:int)->bool:
        s=str(x)
        l,r=0,len(s)-1
        while l<r:
            if s[l]!=s[r]:
                return False
            l,r=l+1,r-1
        return True


x = 12321
sol = Solution2()
print(sol.palindromeNumber(x))
