class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums = sorted(nums)

        for i in range(len(nums)):
            l = i+1
            r = len(nums)-1
            while l<r:
                s=nums[i]+nums[l]+nums[r]

                if s>0:
                    r-=1
                elif s<0:
                    l+=1
                else:
                    candidate = [nums[i],nums[l],nums[r]]
                    if res.count(candidate) == 0:
                        res.append(candidate)
                    l+=1

        return res