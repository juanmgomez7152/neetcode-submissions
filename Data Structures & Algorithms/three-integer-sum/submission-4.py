class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans=[]

        nums.sort()
        print(nums)
        for index,value in enumerate(nums):
            # print(f"Index {index} ; Value {value}")
            l_pointer=index+1
            r_pointer= len(nums)-1
            while l_pointer < r_pointer :
                s = value + nums[l_pointer] +nums[r_pointer]
                if s>0:
                    r_pointer-=1
                elif s<0:
                    l_pointer+=1
                else:
                    triplet = [value, nums[l_pointer], nums[r_pointer]]
                    if ans.count(triplet)==0:
                        ans.append(triplet)
                    l_pointer+=1
        return ans