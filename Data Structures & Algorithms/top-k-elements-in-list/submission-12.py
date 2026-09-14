class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        ans = []
        for n in nums:
            if n in d:
                d[n]+=1
            else:
                d[n]=1
        
        ans = list(dict(sorted(d.items(), key=lambda items:items[1])[::-1][:k]))
        return ans
