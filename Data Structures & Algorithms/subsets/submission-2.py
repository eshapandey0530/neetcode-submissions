class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        # this code only has 1 recurssive function because we are following sequence,
        # do a seperate for loop when all types of combinations are accepted

        n = len(nums)
        result = []

        def backtrack(index, path):

            if index >= n:
                result.append(path[:])
                return

            path.append(nums[index])
            backtrack( index + 1, path)
            path.pop()

            backtrack(index + 1, path)

        backtrack(0, [])

        return result
