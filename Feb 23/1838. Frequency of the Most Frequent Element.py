class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        left = 0
        max_freq = 0
        operations_left = k
        for right in range(n):
            operations_left -= (nums[right] - nums[right-1]) * (right - left)
            while operations_left < 0:
                operations_left += nums[right] - nums[left]
                left += 1
            max_freq = max(max_freq, right - left + 1)
        return max_freq
