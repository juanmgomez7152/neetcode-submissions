class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        res = 0

        while l < r:
            area = min(heights[l], heights[r]) * (r - l)
            res = max(res, area)
            if heights[l] <= heights[r]: # if the left height is smaller or eq to the r height, increse the left pointer
                l += 1
            else:
                r -= 1
        return res