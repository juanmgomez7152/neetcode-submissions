class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref = []
        suff = []
        products = []

        for i in range(len(nums)):
            if i==0:
                pref.append(nums[i])
            else:
                pref.append(pref[i-1]*nums[i])
        nums = nums[::-1]
        for i in range(len(nums)):
            if i==0:
                suff.append(nums[i])
            else:
                suff.append(suff[i-1]*nums[i]) 
        suff = suff[::-1]
        for i in range(len(nums)):
            if i==0:
                products.append(suff[i+1])
            elif i == len(nums)-1:
                products.append(pref[i-1])
            else:
                products.append(pref[i-1]*suff[i+1])

        return products