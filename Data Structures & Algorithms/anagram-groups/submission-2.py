class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answer = defaultdict(list)
        for s in strs:
            sortedstr = ''.join(sorted(s))
            answer[sortedstr].append(s)

        return list(answer.values())