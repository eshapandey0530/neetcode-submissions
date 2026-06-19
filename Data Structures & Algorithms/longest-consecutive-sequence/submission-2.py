class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        s = set(nums)
        res = 0

        for num in s:
            if num-1 not in s:
                count = 1
                next_num = num + 1
                while next_num in s:
                    count += 1
                    next_num += 1
                res = max(res, count)
        
        return res