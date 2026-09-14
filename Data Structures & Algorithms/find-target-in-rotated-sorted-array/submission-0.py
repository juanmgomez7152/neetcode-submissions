class Solution:
    def search(self, nums: List[int], target: int) -> int:
        res = -1
        l,r=len(nums)/2,len(nums)/2

        l = int(l)
        r = int(r)
        while l>=0 or r<=len(nums)-1:
            if l>=0:
                if nums[l] == target:
                    return l

            if r<= len(nums)-1:
                if nums[r] == target:
                    return r
            l-=1
            r+=1
        return res