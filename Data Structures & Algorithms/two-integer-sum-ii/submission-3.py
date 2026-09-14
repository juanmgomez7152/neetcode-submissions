class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l_ptr=0
        r_ptr = len(numbers)-1
        res = []
        while l_ptr<r_ptr:
            s = numbers[l_ptr]+numbers[r_ptr]
            if s == target:
                return [l_ptr+1,r_ptr+1]
            elif s>target:
                r_ptr-=1
            else:
                l_ptr+=1
        return res