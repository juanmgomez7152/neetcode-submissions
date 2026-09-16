class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref = []
        suff = []
        res = []

        pref = self._mult_log(nums,pref)
        nums = nums[::-1]
        suff = self._mult_log(nums,suff)[::-1]

        for i in range(len(nums)):
            if i==0:
                res.append(suff[i+1])
            elif i == len(nums)-1:
                res.append(pref[i-1])
            else:
                res.append(pref[i-1]*suff[i+1])

        return res
    
    def _mult_log(self,nums,new_list):
        for i in range(len(nums)):
            if i == 0:
                new_list.append(nums[i])
            else:
                new_list.append(nums[i]*new_list[i-1])
        return new_list
