class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l_ptr=0
        r_ptr=len(heights)-1
        ans=0
        while l_ptr < r_ptr:
            h = min(heights[l_ptr],heights[r_ptr])
            w = r_ptr - l_ptr
            a = h*w
            ans = max(a,ans)
            if heights[l_ptr]<=heights[r_ptr]:
                l_ptr+=1
            else:
                r_ptr-=1

        return ans