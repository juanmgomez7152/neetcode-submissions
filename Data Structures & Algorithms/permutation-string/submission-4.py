class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1 = sorted(s1)
        r_ptr = len(s1)-1

        for l_ptr in range(len(s2)-r_ptr):
            j = l_ptr+r_ptr
            temp = s2[l_ptr:j+1]
            temp = sorted(temp)
            if temp == s1:
                return True

        return False