class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # time -> O(n)
            # worst O(n) -> after iterating through both strings
            # best O(1) -> when the length is not equal and false is returned in the beginnning
            # O(n) for comparing both the hashmaps

        # space -> O(n)
            # O(n) -> hashmap of s
            # O(n) -> hashmap of t
            # O(n) + O(n) = O(2n) == O(n) in Big - O
            
        if len(s) != len(t):
            return False

        s_count = {}
        t_count = {}

        for letter in s:
            if letter in s_count:
                s_count[letter] += 1
            else:
                s_count[letter] = 1
        
        for letter in t:
            if letter in t_count:
                t_count[letter] += 1
            else:
                t_count[letter] = 1

        if s_count == t_count:
            return True
        else:
            return False