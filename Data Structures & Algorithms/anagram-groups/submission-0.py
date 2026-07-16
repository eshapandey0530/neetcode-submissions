class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 'act' - ['act', 'cat']

        strHashmap = {}

        for s in strs:
            key = "".join(sorted(s))
            if key in strHashmap:
                strHashmap[key].append(s)
            else:
                strHashmap[key] = [s]

        res = []

        for value in strHashmap.values():
            res.append(value)

        return res
