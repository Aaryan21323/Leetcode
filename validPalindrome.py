# Neetcode easy solution using built in functions ... this has o(n) space complexity

class Solution1:
    def isPalindrome(self,s:str)->bool:
        newStr=""

        for c in s:
            if c.isalnum():
                newStr+=c.lower()
        return newStr==newStr[::-1]
    
# Another solution using self made alphanumeric function and using pointers having o(1) space and o(n) time compexity
class Solution:
    def isPalindrome(self,s:str)->bool:
        l,r=0,len(s)-1

        while l<r:
            while l<r and not self.alphaNum(s[l]):
                l+=1
            while r>l and not self.alphaNum(s[r]):
                r-=1
            if s[l].lower()!=s[r].lower():
                return False
            l,r=l+1,r-1
        return True


    def alphaNum(self,c):
        return (ord('A')<=ord(c)<=ord('Z') or ord('a')<=ord(c)<=ord('z') or ord('0')<=ord(c)<=ord('9'))


sol=Solution()
s="racecar"
print(sol.isPalindrome(s))
            