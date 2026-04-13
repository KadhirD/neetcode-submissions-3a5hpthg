class Solution:
    def search(self, nums: List[int], target: int) -> int:
        b, e = 0 , len(nums)-1
        while b <= e:
            m = (b+e)//2
            if nums[m] == target : return m
            if nums[b] <= nums[m]:
                if nums[b] <= target <= nums[m]:
                    e = m-1
                else:
                    b = m+1
            else:
                if nums[m] <= target <= nums[e]:
                    b = m+1
                else:
                    e = m-1
        return -1 
        