class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return "len0"
        return "~`~`~".join(strs)
    def decode(self, s: str) -> List[str]:
        if s =="len0":
            return []
        return s.split("~`~`~")
        
