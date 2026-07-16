class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        # duplicates provided in the array
        # unique combos are allowed to be returned
        # array sum should be equal to target
        # break when the array sum > target

        n = len(candidates)
        result, path = [], []
        candidates.sort()

        def backtracking(index, total):

            if total == target:
                result.append(path[:])
                return
            
            if index == n or total > target:
                return

            for i in range(index, len(candidates)):

                # Skip duplicate numbers
                if i > index and candidates[i] == candidates[i - 1]:
                    continue

                # Choose
                path.append(candidates[i])

                # Move to next index (cannot reuse same number)
                backtracking(i + 1, total + candidates[i])

                # Undo choice
                path.pop()

        backtracking(0, 0)
        # print(result)

        return result