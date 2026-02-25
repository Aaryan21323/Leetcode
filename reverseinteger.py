# my own solution linear time ( convert ot sting and stuff easy i guesss)

class Solution:
 def reverse(self, x: int) -> int:
    if x>0:
     y=str(x)
     x=int(y[::-1])
     if x>2**31-1:
         return 0
     return x
    elif x<0:
      y=str(abs(x))
      x=-int(y[::-1])
      if x<-2**31:
          return 0
      return x
    elif x==0:
        return 0
    
# solution without converting to string and kinda intuative couldn't have thought it myself :)

class Solution1:
    def reverse(self, x: int) -> int:
        max_int32 = 2**31 - 1
        min_int32 = -2**31
        output = 0
        sign = 1 if x >= 0 else -1 # just checknig the sign
        x = abs(x)
        # reverse the string seems easy enough
        while x > 0:
            digit = x % 10
            x = x // 10
            output = output * 10 + digit
            if output > max_int32:
                return 0
        
        return output * sign

x=-1563847412
sol=Solution()
print(sol.reverse(x))