class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_dict = {}
        for n in nums:
            count_dict[n] = 1+count_dict.get(n,0)
        
        desc_counts = dict(sorted(count_dict.items(), key=lambda items:items[1],reverse=True)).keys()
        
        return list(desc_counts)[:k]