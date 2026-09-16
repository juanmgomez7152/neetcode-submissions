class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}

        for i in range(len(nums)):
            nums_dict[i]= nums[i]
        
        nums = list(sorted(nums_dict.items(), key=lambda items:items[1]))
        l=0
        r=len(nums)-1
        while l<r:
            s=nums[l][1]+nums[r][1]
            if s == target:
                return sorted([nums[l][0],nums[r][0]])
            elif s>target:
                r-=1
            else:
                l+=1