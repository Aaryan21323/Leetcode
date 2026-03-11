class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        
        i = 0  # position to insert
        j = 1  # scanner
        
        while j < len(nums):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
            j += 1
        
        return i + 1
    
class Solution1:
    def removeDuplicates(self, nums: list[int]) -> int:
        if not nums:
            return 0
        
        # Slow pointer - points to position where next unique element should go
        slow = 0
        
        # Fast pointer - scans through array
        for fast in range(1, len(nums)):
            if nums[fast] != nums[slow]:
                slow += 1
                nums[slow] = nums[fast]
        
        return slow + 1  # Length is index + 1
    
