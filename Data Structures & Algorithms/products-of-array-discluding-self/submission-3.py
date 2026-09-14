class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref = []
        suff = []
        res = []

        for i in range(len(nums)):
            if i == 0:
                pref.append(nums[0])
            else:
                pref.append(nums[i]*pref[i-1])
        nums_rvrs = nums[::-1]
        for i in range(len(nums_rvrs)):
            if i == 0:
                suff.append(nums_rvrs[0])
            else:
                suff.append(nums_rvrs[i]*suff[i-1])
        suff =suff[::-1]
        for i in range(len(nums)):
            if i == 0:
                res.append(suff[i+1])
            elif i == (len(nums)-1):
                res.append(pref[i-1])
            else:
                res.append(pref[i-1]*suff[i+1])
        return res       