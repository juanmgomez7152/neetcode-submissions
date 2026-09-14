class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ans=0
        for i,a in enumerate(heights):
            r = len(heights)-1
            while r != i:
                h = min(heights[r],a)
                w = r-i
                v = h*w
                if v>ans:
                    ans=v
                r-=1

                

        return ans