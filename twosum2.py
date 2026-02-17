# brute force b takes more time
class Solution1:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        for i in range(len(numbers)):
            for j in range(i + 1, len(numbers)):
                if numbers[i] + numbers[j] == target:
                    return [i + 1, j + 1]   
        
        return []
    

#neetcode solution using pointers
class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
       l,r=0,len(numbers)-1

       while l<r:
        currentSum=numbers[l]+numbers[r]

        if currentSum>target:
            r-=1
        elif currentSum<target:
            l+=1
        else:
            return [l+1,r+1]
       return []  
                 