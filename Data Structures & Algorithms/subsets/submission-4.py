class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        # this code only has 1 recurssive function because we are following sequence,
        # do a seperate for loop when all types of combinations are accepted

        def backtrack(index, n, path, result):

            if index >= n:
                result.append(path[:])  # [:] because path is passed as a reference
                return

            # picked
            path.append(nums[index])
            backtrack( index + 1, n, path, result)
            path.pop()

            # not picked
            backtrack(index + 1, n, path, result)

            return result

        return backtrack(0, len(nums), [], [])
