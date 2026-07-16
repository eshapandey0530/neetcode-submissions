class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if s == '' and t == '':
            return True
        if s == '' or t == '':
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