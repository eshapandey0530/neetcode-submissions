class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        # open bracket == closed brackets
        # combination can start only from opening bracket
        # n = 1 == '()'

        result, path = [], []

        def backtrack(curr_str, open_count, close_count):
            if len(curr_str) == 2*n:
                result.append(curr_str)
                return

            if open_count < close_count:
                backtrack(curr_str + ')', open_count, close_count - 1)
            
            if open_count > 0:
                backtrack(curr_str + '(', open_count - 1, close_count)

            return result

        return backtrack('', n, n)

        