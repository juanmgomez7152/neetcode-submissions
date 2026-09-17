class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res=[]

        for i in range(len(nums)):
            l=i+1
            r=len(nums)-1
            while l<r:
                pair = [nums[i],nums[l],nums[r]]
                s = sum(pair)
                if s==0:
                    if pair not in res:
                        res.append(pair)
                elif s>0:
                    r-=1
                    continue
                
                l+=1
                

        return res