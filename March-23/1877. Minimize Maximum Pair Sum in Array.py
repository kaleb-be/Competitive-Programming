class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        max_sum = float('-inf')
        left, right = 0, n - 1
        while left < right:
            pair_sum = nums[left] + nums[right]
            max_sum = max(max_sum, pair_sum)
            left += 1
            right -= 1
        return max_sum
