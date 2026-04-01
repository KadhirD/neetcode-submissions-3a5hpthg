class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            prd =1
            for j in range(len(nums)):
                if i==j:
                   continue
                else:
                    prd = prd * nums[j]
            res.append(prd)
        return res
        