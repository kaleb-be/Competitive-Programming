class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        target_idx=[]
        for i in range(len(sorted(nums))):
            if sorted(nums)[i] == target:
                target_idx.append(i)
        return target_idx
        
