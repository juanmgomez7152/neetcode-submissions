class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        answer = defaultdict(int)
        for num in nums:
            answer[num]+=1
        
        answer = dict(sorted(answer.items(),key=lambda item:item[1],reverse=True))# this is still a dict
        print(answer) #dictionary of key and # of occurences. This is sorted in descending order based on the values (values is referenced in "item[1]", if it was "item[0]" it wouldve been sorted based on keys)
        answer = list(answer)
        print(answer) #list of only the keys
        return answer[:k]