class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        result, path = [], []
        n = len(nums)

        def backtrack():

            if len(path) == n:
                result.append(path[:])
                return

            for i in nums:
                if i not in path:
                    path.append(i)
                    backtrack()
                    path.pop()
            
        backtrack()

        return result
        