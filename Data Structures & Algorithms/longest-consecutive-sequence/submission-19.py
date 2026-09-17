class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(set(nums))
        res =0
        c=1
        if not nums or len(nums)==1:
            return len(nums,)
        for i in range(len(nums[:len(nums)-1])):
            diff = abs(nums[i+1]-nums[i])
            print(diff)
            if diff==1:
                c+=1
            else:
                res = max(res,c)
                c=1
        res = max(res,c)
        return res
