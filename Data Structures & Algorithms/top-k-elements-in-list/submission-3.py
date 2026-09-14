class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        res = []

        for num in nums:
            d[num] = d.get(num,0)+1
        sorted_d = sorted(d.items(), key=lambda x:x[1],reverse=True)[:k]
        
        for num in sorted_d:
            res.append(num[0])
        return res