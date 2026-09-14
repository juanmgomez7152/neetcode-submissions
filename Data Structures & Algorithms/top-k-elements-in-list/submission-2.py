class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res=[]
        d={}

        for num in nums:
            if num in d:
                d[num]+=1
            else:
                d[num]=1
        
        d = sorted(d.items(), key= lambda x:x[1], reverse=True)[:k]
        
        for num in d:
            res.append(num[0])
        return res