class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        count,prd = 0,1
        for i in range(len(nums)):
            if nums[i] == 0:
                count += 1
            else : prd *=nums[i]

        if count>1 :
            return ([0]*len(nums))
        
        res = [0] * len(nums)
        if count ==1 :
            res[nums.index(0)] = prd
            return (res)
        for j,c in enumerate(nums):
            res[j] = prd//c
        return res
        