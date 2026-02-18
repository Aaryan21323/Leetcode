# brute force solution having time complexity O(n^3) this doesn.t work in leetcode due to time limit exceeded 

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        soln = set()
        n = len(nums)

        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if nums[i] + nums[j] + nums[k] == 0:
                        triplet = tuple(sorted([nums[i], nums[j], nums[k]]))
                        soln.add(triplet)

        return [list(t) for t in soln]
    
# neetcode solution with time complexity o(n^2)

class Solution:
    
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res=[]
        nums.sort() # first we sort the list

        for i,a in enumerate(nums): # enumererate returns bith the index and the value
            if i>0 and a==nums[i-1]: # checking if the num are duplicate or not
                continue
            l,r=i+1,len(nums)-1  #using pointer l and r same as in twosum2
            while l<r:
                threesum=a+nums[l]+nums[r] # finding the three sum
                if threesum>0:  # if three sum greater than 0 we decrease the right ponter as we need less total value
                 r-=1
                elif threesum<0:# if three sum lesser than 0 we increase the left pointer as we need more total value
                 l+=1
                else:
                  res.append([a,nums[l],nums[r]]) # if three sum is equal to 0 then we append the num to the list as a list
                  l+=1
                  while nums[l]==nums[l-1] and l<r: # this condition is used to check and increase the l pointer when an soln is found and to find other solns
                     l+=1
        return res 
        



        