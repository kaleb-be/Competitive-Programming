class Solution:
    def maxArea(self, height: List[int]) -> int:
        l_ptr , r_ptr = 0, len(height) -1
        area = 0
        while l_ptr < r_ptr:
            h = min(height[r_ptr], height[l_ptr])
            area = max(area, (r_ptr - l_ptr)*h)
            if height[r_ptr]<height[l_ptr]:
                r_ptr -=1
            else: l_ptr += 1
        return area
