class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ans=0
        l_ptr = 0
        r_ptr = len(heights)-1

        while l_ptr<r_ptr:
            w = r_ptr - l_ptr
            h = min(heights[l_ptr],heights[r_ptr])
            a = w*h
            ans = max(ans,a)

            if heights[l_ptr]<=heights[r_ptr]:
                l_ptr+=1
            else:
                r_ptr-=1


        return ans