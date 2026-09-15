class Solution:
    def maxArea(self, heights: List[int]) -> int:
        m = 0
        l=0
        r=len(heights)-1

        while l<r:
            height = min(heights[l],heights[r])
            width = r-l
            area = height*width
            m = max(m,area)

            if heights[l]>=heights[r]:
                r-=1
            else:
                l+=1
        
        return m