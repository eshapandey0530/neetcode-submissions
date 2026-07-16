class Solution:
    def climbStairs(self, n: int) -> int:
        one = 1
        two = 1

        for i in range(n - 1):
            temp = two
            two = one + temp
            one = temp

        return two

        # prev, curr = 1,1

        # for i in range(n-1):
        #     temp = curr
        #     curr = prev+temp
        #     prev = temp
        # return curr
