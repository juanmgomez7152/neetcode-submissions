class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = collections.defaultdict(int)
        res = []
        for n in nums:
            d[n]+=1

        d=list(sorted(d.items(),key= lambda x:x[1], reverse=True))
        for i in range(k):
            res.append(d[i][0])
        return res
