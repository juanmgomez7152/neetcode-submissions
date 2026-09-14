class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ans = 0
        temp=0
        nums.sort()
        print(nums)
        i = 0
        for i in range(len(nums)):
            temp+=1
            j=i+1
            if j<(len(nums)):
                # print(f"Temp = {temp}")
                val_dif = nums[j]-nums[i]
                if val_dif>1:
                    ans = max(ans,temp)
                    temp = 0
                elif val_dif<1:
                    temp-=1
            else:
                ans = max(ans,temp)
            print(f"Temp = {temp}")

            i+=1
        return ans