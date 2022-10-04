class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        next_non_zero = 0
    
        for ptr in range(len(nums)):
            if nums[ptr] != 0:
                nums[next_non_zero], nums[ptr] = nums[ptr], nums[next_non_zero]
                next_non_zero += 1
            
            ptr += 1
            
        return nums
