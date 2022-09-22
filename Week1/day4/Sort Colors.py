class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i, j, target, n = 0,0,1, len(nums)-1
        while j <= n:
            if nums[j] < target:
                nums[j], nums[i] = nums[i], nums[j]
                i+=1
                j+=1
            elif nums[j] > target:
                nums[j], nums[n] = nums[n], nums[j]
                n-=1
            else:
                j+=1

if __name__ == "__main__":
    colors = [2, 1, 1, 0, 0, 2]
    Solution().sortColors(colors)
    print(A)
