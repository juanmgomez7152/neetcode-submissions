class Solution:
    def isPalindrome(self, s: str) -> bool:
        temp  = ""
        s= s.lower()
        for c in s:
            if c.isalnum():
                temp+=c

        return temp == temp[::-1]