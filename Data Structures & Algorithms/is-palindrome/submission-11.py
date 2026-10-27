class Solution:
    def isPalindrome(self, s: str) -> bool:
        letters_arr = []

        for c in s:
            if c.isalnum():
                letters_arr.append(c.lower())

        return letters_arr == letters_arr[::-1]