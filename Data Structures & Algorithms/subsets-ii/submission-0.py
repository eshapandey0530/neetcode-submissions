class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        n = len(nums)
        result, path = [],  []

        def backtracking(i):

            result.append(path[:])

            for j in range(i, n):

                if j > i and nums[j] == nums[j-1]:
                    continue

                path.append(nums[j])
                backtracking(j+1)
                path.pop()

        backtracking(0)

        return result
        