class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res=[]
        l_arr=[]
        r_arr=[]

        for i in range(len(nums)):
            if i==0:
                l_arr.append(nums[i])
            else:
                l_arr.append(nums[i]*l_arr[i-1])
        
        nums = nums[::-1]
        for i in range(len(nums)):
            if i == 0:
                r_arr.append(nums[i])
            else:
                r_arr.append(nums[i]*r_arr[i-1])

        r_arr=r_arr[::-1]

        for i in range(len(nums)):
            if i==0:
                res.append(r_arr[i+1])
            elif i == len(nums)-1:
                res.append(l_arr[i-1])
            else:
                res.append(l_arr[i-1]*r_arr[i+1])

        return res