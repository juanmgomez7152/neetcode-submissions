class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        d ={}
        for num in nums:
            if num in d.keys():
                d[num]+=1
            else:
                d[num] = 1

        d = list(sorted(d.items(),key=lambda x:x[1], reverse=True))[:k]
        for pair in d:
            res.append(pair[0])
        return res