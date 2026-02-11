# brute force

class Solution1:
    def topkfrequency(self,nums:list[int],k:int):
        
        freq={}

        for num in nums:
            if num in freq:
             freq[num]+=1
            else:
               freq[num]=1

        sorted_nums=sorted(freq,key=freq.get,reverse= True)

        return sorted_nums[:k]
    

# neetcode Solution Bubbble Sort Method

class Solution:
   def topKFrequent(self,nums:list[int],k:int)->list[int]:
      count={}
      
      freq=[[] for i in range(len(nums)+1)]

      for n in nums:
         count[n]=1+count.get(n,0)
      for n,c in count.items():
         freq[c].append(n)
    
      res=[]

      for i in range(len(freq)-1,0,-1):
         for n in freq[i]:
            res.append(n)
            if len(res)==k:
               return res
   

    


nums=[1,1,1,1,2,2,3,3,4,5]
k=3

sol=Solution()

print(sol.topKFrequent(nums,k))
