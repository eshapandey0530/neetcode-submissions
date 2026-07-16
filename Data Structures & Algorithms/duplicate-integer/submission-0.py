class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        # time -> O(n) - only iterating once
        # space -> worst case O(n) - if no duplicates are found all will be added to set_nums
        set_nums = set()

        for num in nums:
            if num in set_nums:
                return True
            else:
                set_nums.add(num)

        return False