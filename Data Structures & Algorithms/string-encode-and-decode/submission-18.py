class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return"0"
        else:
            return '`~`~`'.join(strs)
    def decode(self, s: str) -> List[str]:
        if s == "0":
            return []
        else:
            return s.split('`~`~`')