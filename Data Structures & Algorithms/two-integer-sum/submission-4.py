class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        n = len(nums)

        hmap = {}

        for i in range(n):

            diff = target - nums[i]
            if diff in hmap:
                return [hmap[diff], i]
            else:
                hmap[nums[i]] = i


        # while l <= r:
        #     s = nums[l] + nums[r]
        #     if s == target:
        #         return [l,r]
        #     elif s > target:
        #         r -= 1
        #     else:
        #         l += 1

        # return [l,r]
