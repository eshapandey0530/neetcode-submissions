class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # brute force - nested loop - all pairs are compared -> ~O(n^2)
        # space -> O(1)
        # works for sorted and unsorted array

        # uses hashmap for maintaing and saving indexes
        # 2 ways -> either create a hashmap in the beginning and put a condition to check the indexes are not same
            # or -> add the index and element in the hashmap one by one as we check the difference is existing in the array or not

        hashmap = {}

        for i in range(len(nums)):
            
            diff = target - nums[i]

            if diff in hashmap:
                return [hashmap[diff], i]

            else:
                hashmap[nums[i]] = i

        return None
        