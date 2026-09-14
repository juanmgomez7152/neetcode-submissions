class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res=0
        l_ptr=0
        r_ptr=len(heights)-1

        while l_ptr < r_ptr:
            area = min(heights[l_ptr],heights[r_ptr])*(r_ptr-l_ptr)
            res = max(res,area)
            if heights[l_ptr]<=heights[r_ptr]:
                l_ptr += 1
            else:
                r_ptr -= 1

        return res