class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        hset = set(nums)
        res = 0

        for n in nums:
            if n - 1 not in hset:
                count = 1
                next_n = n + 1
                while next_n in hset:
                    count += 1
                    next_n += 1
                res = max(res, count)

        return res
