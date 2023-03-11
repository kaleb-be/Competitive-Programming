class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        def can_form_arithmetic_sequence(nums):
            # Create a dictionary to count the frequency of each number
            freq = {}
            for num in nums:
                freq[num] = freq.get(num, 0) + 1

            # Sort the subarray
            nums.sort()

            # Check if the difference between every two consecutive elements is the same
            diff = nums[1] - nums[0]
            for i in range(1, len(nums)):
                if nums[i] - nums[i-1] != diff:
                    return False

            return True

        def check_arithmetic_subarray(nums, l, r):
            # Get the subarray
            subarray = nums[l:r+1]

            # Check if it can form an arithmetic sequence
            if can_form_arithmetic_sequence(subarray):
                return True

            return False

        
        # Initialize the list of answers
        answers = []

        # Check each query
        for i in range(len(l)):
            if check_arithmetic_subarray(nums, l[i], r[i]):
                answers.append(True)
            else:
                answers.append(False)

        return answers
