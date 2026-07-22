class Solution:

    def encode(self, strs: List[str]) -> str:

        code = ''

        if len(strs) == 0:
            return ''
        
        for s in strs:
            str_len = str(len(s))
            code += str_len + '#' + s
        
        print(code)
        return code

    def decode(self, s: str) -> List[str]:

        if len(s) == 0:
            return []

        res = []

        i = 0
        while i < (len(s)):
            j = i
            while s[j] != '#':
                j += 1

            length = int(s[i:j])
            res.append(s[j + 1 : j + length + 1])
            i = j + length + 1

        return res