# neetcode solution
class Solution:
    def longestSequence(self,nums:list[int])->int:
        numSet=set(nums)
        longest=0

        for n in nums:
            if (n-1) not in numSet:
                length=0
                while (n+length) in numSet:
                    length+=1
                longest=max(length,longest)
        return longest
    
sol=Solution()
nums=[100,4,200,1,3,2]
print(sol.longestSequence(nums))