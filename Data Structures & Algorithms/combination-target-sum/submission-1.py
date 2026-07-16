class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        n = len(nums)
        res, path = [], []

        # a subset array needs to be passed which totals to the target sum
        # total sum needs to be passed as well
        # elements can be repeated so duplicates are allowed

        def backtrack(i, total):
            if total == target:
                res.append(path[:])
                return

            if i == n or total > target:
                return

            # not include
            backtrack(i+1, total)

            # include
            path.append(nums[i])
            backtrack(i, total + nums[i])
            path.pop()

        backtrack(0, 0)

        return res
