class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        pairs = {}
        count = 0
        
        for num in nums:
            if k - num in pairs and pairs[k - num] > 0:
                pairs[k - num] -= 1
                count += 1
            else:
                if num in pairs:
                    pairs[num] += 1
                else:
                    pairs[num] = 1
        
        return count
