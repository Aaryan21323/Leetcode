# brute force method time complexity:O(n^2) doesn't work in leetcode time limit exceeds

class Solution:
    def maxArea(self,height:list[int])->int:
        res=0
        for l in range(len(height)):
            for r in range(l+1,len(height)):
                area=(r-1)*min(height[l],height[r])
                res=max(res,area)

        return res
    
#neetcode solution linear time complexity O(n)
class Solution:
   def maxArea(self,height:list[int])->int:
    res=0
    l,r=0,len(height)-1
    while l<r:
       area=(r-l)*min(height[l],height[r])
       res=max(res,area)
       if height[l]<height[r]:
          l+=1
       else:
          r-=1
    return res

