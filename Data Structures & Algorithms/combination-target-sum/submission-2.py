class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        # a subset array needs to be passed which totals to the target sum
        # total sum needs to be passed as well
        # elements can be repeated in the final array, so duplicates are allowed

        def backtrack(index, n, total, path, result):
            if total == target:
                result.append(path[:])
                return
            
            if index >= n or total > target:
                return

            # picked
            path.append(nums[index])
            backtrack(index, n, total + nums[index], path, result)
            path.pop()

            # not picked
            backtrack(index + 1, n, total , path, result)

            return result

        return backtrack(0, len(nums), 0, [], [])
