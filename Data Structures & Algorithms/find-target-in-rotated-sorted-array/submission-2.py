class Solution:
    def search(self, nums: List[int], target: int) -> int:
        res = -1
        l_ptr=0
        r_ptr=len(nums)-1

        while l_ptr<=r_ptr:
            if nums[l_ptr] == target:
                return l_ptr
            elif nums[r_ptr] == target:
                return r_ptr
            else:
                l_ptr+=1
                r_ptr-=1

        return res