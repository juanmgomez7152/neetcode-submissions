class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        answer = defaultdict(int)
        for num in nums:
            answer[num]+=1
        
        answer = dict(sorted(answer.items(),key=lambda item:item[1],reverse=True))
        answer = list(answer)
        return answer[:k]