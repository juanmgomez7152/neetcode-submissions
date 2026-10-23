class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_d = {}
        ans = []
        for n in nums:
            count_d[n] = count_d.get(n,0)+1

        count_d = (sorted(count_d.items(),key=lambda items:items[1], reverse=True)[:k])       
        for p in count_d:
            ans.append(p[0])

        return ans