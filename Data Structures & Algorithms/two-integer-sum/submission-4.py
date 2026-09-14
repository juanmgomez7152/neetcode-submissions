class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {}
        for i in range(len(nums)):
            m[i]=nums[i]
        m = list(sorted(m.items(), key=lambda item:item[1]))
        l=0
        r=len(m)-1
        while l<r:
            s = m[l][1] + m[r][1]
            if s==target:
                return sorted([m[l][0],m[r][0]])
            elif s>target:
                r-=1
            else:
                l+=1
        