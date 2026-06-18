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