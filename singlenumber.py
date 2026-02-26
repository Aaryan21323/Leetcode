# my own solution
class Solution:
    def singleNumber(self, nums: list[int]) -> list:
        count={} # create a hash map count to count all the occurrences of the numbers, which simply creates a key value pair like {4:1,2:2...} we just have to iterate and find the number which has 1 count as the question suggests 
        min=0
        l=0

        for r in range(len(nums)):
            count[nums[r]]=1+count.get(nums[r],0) # increase the key value if the number is detexted in the list, this is the most important part
            
        for x,y in count.items(): # iterate through the hashmap 
            if y==1: # if the count/value is equal to 1 min = key 
                min=x
            
        return min # return the key


sol=Solution()
nums = [4,1,2,1,2]
print(sol.singleNumber(nums))