class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums = sorted(nums)

        for i in  range(len(nums)):
            l_ptr = i+1
            r_ptr = len(nums)-1

            while l_ptr < r_ptr:
                s = nums[i]+nums[l_ptr]+nums[r_ptr]
                if s<0:
                    l_ptr+=1
                elif s>0:
                    r_ptr-=1
                else:
                    candidate = [nums[i],nums[l_ptr],nums[r_ptr]]
                    if res.count(candidate) == 0:
                        res.append(candidate)
                    l_ptr+=1

        return res