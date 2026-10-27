class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ans = 0
        nums = sorted(set(nums))
        if len(nums) == 0:
            return ans
        curr = 1
        for i in range(len(nums)-1):
            if nums[i+1]-nums[i] == 1:
                curr+=1
            else:
                ans = max(ans,curr)
                curr = 1
        ans = max(ans,curr)
        return ans