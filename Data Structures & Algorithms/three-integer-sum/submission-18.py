class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        ans = []

        for i in range(len(nums)-2):
            l_ptr = i+1
            r_ptr = len(nums)-1
            while l_ptr < r_ptr:
                tri_sum = nums[i]+nums[l_ptr]+nums[r_ptr]
                if tri_sum == 0:
                    candidates = [nums[i],nums[l_ptr],nums[r_ptr]]
                    if candidates not in ans:
                        ans.append(candidates)
                    r_ptr-=1
                elif tri_sum<0:
                    l_ptr+=1
                else:
                    r_ptr-=1


        return ans