# my own solution convert to integer and then add and again convert to binary sting
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        intNum1=int(a,2)
        intNum2=int(b,2)
        sum=intNum1+intNum2
        return format(sum,'b')
    
sol=Solution()
a="11"
b="1"
print(sol.addBinary(a,b))