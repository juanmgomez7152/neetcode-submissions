class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res=0
        if not nums:
            return res
        nums = list(sorted(set(nums)))
        print(nums)
        c=1
        for i in range(len(nums)-1):
            if abs(nums[i+1]-nums[i])!=1:
                res = max(res,c)
                c=1
            else:
                c+=1

        res=max(res,c)

        return res