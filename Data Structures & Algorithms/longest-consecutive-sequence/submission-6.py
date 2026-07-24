class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        # iterate through the array
        # check previous number exist or not in the array from the current selection
        # when found a starting point, start checking for the consecutive sequence
        # use a count variable to keep a track 
        # use hash set to check visited numbers

        # edge cases
            # null
            # single
            # unsorted
            # negatives
            # mixed sign
            # no consecutives
            # multiple consecutives

        # checking in hashset and not the list because lookup is O(1)

        hset = set(nums)
        res = 0

        for num in nums:

            if num - 1 not in hset:
                count = 1
                next_num = num + 1
                while next_num in hset:
                    count += 1
                    next_num += 1
                res = max(res, count)

        return res



















        # hset = set(nums)
        # res = 0

        # for n in nums:
        #     if n - 1 not in hset:
        #         count = 1
        #         next_n = n + 1
        #         while next_n in hset:
        #             count += 1
        #             next_n += 1
        #         res = max(res, count)

        # return res
