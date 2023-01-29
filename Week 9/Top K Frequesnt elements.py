import collections
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = collections.Counter(nums)
        freq = dict(sorted(freq.items(), key=lambda x:x[-1]))
        return list(freq.keys())[-k::]
