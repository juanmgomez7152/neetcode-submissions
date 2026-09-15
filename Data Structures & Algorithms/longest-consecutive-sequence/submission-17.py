class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        if nums==[] or len(nums)==1:
            return len(nums)
        nums = sorted(set(nums))
        c=0
        for i in range(len(nums)):
            if i == 0:
                c+=1
            elif (nums[i]-nums[i-1])!=1:
                res = max(res,c)
                c=1
            else:
                c+=1
        res = max(res,c)
        return res