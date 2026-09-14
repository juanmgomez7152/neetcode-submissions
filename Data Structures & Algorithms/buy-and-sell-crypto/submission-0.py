class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r=1
        max_p = 0
        while r < len(prices):
            if prices[l]<prices[r]: # only do profit calc if right price is greater
                p = prices[r] - prices [l]
                max_p = max(max_p, p)
            else: #if left price is greater or equal make l and r the same
                l=r
            r+=1 #auto increase r pointer to be able to escape the while loop
        return max_p