class Solution:
    def isPalindrome(self, s: str) -> bool:
        alpha_str = ""
        s=s.lower()
        for char in s:
            if char.isalpha() or char.isalnum():
                alpha_str+=char
        reverse_str = alpha_str[::-1]
        print(reverse_str)
        print(alpha_str)
        if reverse_str == alpha_str:
            return True
        else:
            return False