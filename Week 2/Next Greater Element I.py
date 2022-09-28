class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        for i in nums1:
            NGE = -1
            for j in nums2[nums2.index(i):]:
                if j>i:
                    NGE = j
                    break
            ans.append(NGE)
        return ans
