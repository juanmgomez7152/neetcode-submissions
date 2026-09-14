class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        pref = []
        suf = []

        for i in range(len(nums)):
            if i==0:
                pref.append(nums[i])
            else:
                pref.append(nums[i]*pref[i-1])
        nums_rvrs = nums[::-1]
        for i in range(len(nums)):
            if i==0:
                suf.append(nums_rvrs[i])
            else:
                suf.append(nums_rvrs[i]*suf[i-1])
        
        suf = suf[::-1]
        for i in range(len(nums)):
            if i==0:
               res.append(suf[i+1])
            elif i==(len(nums)-1):
                res.append(pref[i-1])
            else:
                res.append(suf[i+1]*pref[i-1])

        return res