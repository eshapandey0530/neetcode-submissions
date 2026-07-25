class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        hmap = {}
        n = len(nums)

        for i in range(n):
            hmap[nums[i]] = i

        res = []

        for i in range(n-1):

            for j in range(i + 1, n):

                diff = (- nums[i] - nums[j])

                if diff in hmap:
                    k = hmap[diff]

                    if k != i and k != j:
                        final = sorted([nums[i], nums[j], nums[k]])

                        if final not in res:
                            res.append(final)

        return res
                    


