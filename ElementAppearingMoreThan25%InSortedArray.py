class Solution:
    def findSpecialInteger(self, arr: list[int]) -> int:
        tf=(0.25*(len(arr)+1))
        count={}

        for i in range(len(arr)):
            count[arr[i]]=1+count.get(arr[i],0)

        for x,y in count.items():
            if y>tf or y==tf:
                return x
            
            