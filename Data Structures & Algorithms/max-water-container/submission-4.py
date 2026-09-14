class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ans=0 #initialize the response
        for i,a in enumerate(heights): #i will be the left pointer that auto increases
            r = len(heights)-1 #est the r pointer
            while r != i: # stop once the l and r pointer are the same
                h = min(heights[r],a) # to prevent overflow, the max height is the smallest of the height vals
                w = r-i #width is the difference in index, since i != r, then its always non zero width
                v = h*w 
                ans = max(v, ans) #change ans if v is larger
                r-=1 # decrease the r pointer to escape the while loop eventually

        return ans