class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        if (not len(nums) or not sum(nums)):
            return "0"
        elif (len(nums) == 1):
            return str(nums[0])
        dic = {}
        result = ""
        nums = [str(x) for x in nums]

        # return -1 to get first case
        def comp(s1,s2):
            if (s1 + s2) > (s2 + s1):
                return -1
            return 1 

        nums = sorted(nums,key=cmp_to_key(comp))
        
        return "".join(nums)
