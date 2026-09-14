class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = False
        s = s.lower()
        valid_str = ""
        for c in s:
            if c.isalnum():
                valid_str+=c
        
        return valid_str == valid_str[::-1]