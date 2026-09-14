class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_dict = collections.defaultdict(int)
        res = []
        for n in nums:
            count_dict[n]+=1
        

        count_dict = sorted(count_dict.items(),key=lambda x:x[1],reverse=True)[:k]

        for c in count_dict:
            res.append(c[0])

        return res

