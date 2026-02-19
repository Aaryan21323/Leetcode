# my own solution cannot believed it worked :) ( This could be done in less code i guess)
class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        stringNum="" # creating empty stringNum ( so that we can convert the int in the digits list into a string of number )
        soln=[]  # The solution list that will be outputed
        for s in range(len(digits)): # this is to convert the array elements into a string
            stringNum+=str(digits[s]) # simply using the conversion to convert the int to str and append to the empty stingNum
            
        strtonum=int(stringNum) # converting the string back to int for addition with one
        plusone=strtonum+1   # the plus one that is actually needed
        numtostr=str(plusone) #again converting the plusOne int to str
        
        for s in numtostr: # this convert the str into an int and append to the soln list
            soln.append(int(s))
        return soln  # return the solution
    
sol=Solution()
digits=[1,2,3]
print(sol.plusOne(digits))