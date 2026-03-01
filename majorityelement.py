# my own solution faster why weird ??
class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        major=0
        majorInt=0
        hashSet={}

        for i in range(len(nums)):
            hashSet[nums[i]]=1+hashSet.get(nums[i],0)
            
        
        for x,y in hashSet.items():
          if y>major:
            major=y  
            majorInt=x

        return majorInt
        

# my own solution don't know why it's slow

class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        major=0
        majorInt=0
        hashSet={}

        for i in range(len(nums)):
            hashSet[nums[i]]=1+hashSet.get(nums[i],0)
            if hashSet[nums[i]]>major:
                major=hashSet[nums[i]]
                majorInt=nums[i]
        
        

        return majorInt
    


sol=Solution()
nums = [2,2,1,1,1,2,2]
print(sol.majorityElement(nums))