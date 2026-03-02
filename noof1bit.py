# my own solution
class Solution:
    def hammingWeight(self, n: int) -> int:
        count=0  # intialize count for number of 1's
        binaryInt=format(n,'b') # convert the int to binary string easier in python

        for i in binaryInt: # loop through the binaryInt String 
            if i=='1':
                count+=1  # increment count if 1 is encountered
        return count # return the count of 1's