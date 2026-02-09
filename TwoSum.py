# brute force

class Solution1:
    def twoSum(self,a:list[int],t:int)-> list[int]:
     for i in range(len(a)):
        for j in range(i+1,len(a)):
         if a[i]+a[j]==t:
           return [i,j]
         else:
           i=+1


# neetcode solution
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        prevMap={}

        for i,n in enumerate(nums):
            diff=target-n
            if diff in prevMap:
                return [prevMap[diff],i]
            prevMap[n]=i # update the hash map

         

a=[1,2,3,6]
t=5

sr= Solution()
print(sr.twoSum(a,t))


