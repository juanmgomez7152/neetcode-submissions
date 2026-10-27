class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        pref = []
        suff = []

        for i in range(len(nums)):
            if i == 0:
                pref.append(nums[i])
            else:
                pref.append(nums[i]*pref[i-1])
        # print(f"pref {pref}")
        nums = nums[::-1]
        for i in range(len(nums)):
            if i == 0:
                suff.append(nums[i])
            else:
                suff.append(nums[i]*suff[i-1])
        
        suff = suff[::-1]
        # print(f"suff {suff}")
        for i in range(len(nums)):
            if i == 0:
                ans.append(suff[i+1])
            elif i == len(nums)-1:
                ans.append(pref[i-1])
            else:
                ans.append(pref[i-1]*suff[i+1])


        return ans
        