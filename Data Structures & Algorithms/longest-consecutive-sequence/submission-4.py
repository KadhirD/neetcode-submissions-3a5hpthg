class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0

        for i in nums:
            if (i-1) not in num_set:
                next_num = i+1
                length = 1
                while next_num in num_set:
                    next_num +=1
                    length +=1
                longest = max(longest,length)
        return longest
