class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums = sorted(nums)
        for i in range(len(nums)):
            l=i+1
            r=len(nums)-1
            while l<r:
                s = nums[i]+nums[l]+nums[r]
                if s == 0:
                    candidate = [nums[i],nums[l],nums[r]]
                    if candidate not in ans:
                        ans.append(candidate)
                    l+=1
                elif s>0:
                    r-=1
                else:
                    l+=1
        
        return ans
