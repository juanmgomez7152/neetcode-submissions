class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        letter_count = {}
        ans=0
        l_ptr=0

        for r_ptr in range(len(s)):
            letter_count[s[r_ptr]] = letter_count.get(s[r_ptr],0)+1
            while ((r_ptr-l_ptr+1)-max(letter_count.values()))>k:
                letter_count[s[l_ptr]]-=1
                l_ptr+=1

            ans = max(ans,(r_ptr-l_ptr+1))


        return ans