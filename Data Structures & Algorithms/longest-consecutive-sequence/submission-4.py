class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        res = 0

        nums = sorted(set(nums))
        c=1
        for i in range(len(nums[:(len(nums)-1)])):
            if nums[i+1] - nums[i] == 1:
                c+=1
            else:
                res = max(res,c)
                c = 1
        
        res = max(res,c)

        return res