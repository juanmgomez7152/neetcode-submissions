class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        res = []
        for num in nums:
            c = d.get(num,None)
            if c:
                d[num]+=1
            else:
                d[num]=1

        keys_sorted = sorted(list(d.items()), key=lambda x:x[1],reverse=True)

        for key in keys_sorted:
            res.append(key[0])

        return res[:k]