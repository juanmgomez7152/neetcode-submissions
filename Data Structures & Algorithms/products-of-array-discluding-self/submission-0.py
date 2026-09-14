class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        i = 0

        while i < len(nums):
            print(i)
            j=0
            temp2=1
            while j<len(nums):
                if j != i:
                    temp1 = nums[j]
                    temp2 = temp1 *temp2
                j+=1
            res.append(temp2)
            i+=1
        return res