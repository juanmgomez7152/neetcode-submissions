class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l_ptr = 0
        r_ptr = len(heights)-1
        res=0

        while l_ptr<r_ptr:
            width = r_ptr-l_ptr
            height = min(heights[l_ptr],heights[r_ptr])
            area = height*width
            res = max(res,area)

            if heights[r_ptr]>=heights[l_ptr]:
                l_ptr+=1
            else:
                r_ptr-=1
        return res