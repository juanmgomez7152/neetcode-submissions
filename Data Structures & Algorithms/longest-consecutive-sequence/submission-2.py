class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0 
        if len(nums)==0:
            return res

        nums = sorted(set(nums))
        c=1
        for i in range(len(nums[:(len(nums)-1)])):
            diff = nums[i+1]-nums[i]
            if diff == 1:
                c+=1
            else:
                res=max(res,c)
                c=1

        res = max(res,c)
        return res