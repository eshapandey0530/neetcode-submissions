class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        prefix = [0 for i in range(n)]     # left end
        postfix = [0 for i in range(n)]    # right end

        multiplier = 1
        for i in range(n):

            if i == 0:
                prefix[0] = multiplier
            else:
                multiplier *= nums[i-1]
                # print(multplier)
                prefix[i] = multiplier

        
        multiplier = 1
        for i in range(n-1, -1, -1):

            if i == n-1:
                postfix[i] = multiplier
            else:
                multiplier *= nums[i+1]
                postfix[i] = multiplier

        print(prefix)
        print(postfix)

        result = []
        for i in range(n):
            result.append(prefix[i] * postfix[i])

        return result





