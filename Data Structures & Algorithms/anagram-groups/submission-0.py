class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hmap = {}

        n = len(strs)

        for s in strs:
            l = sorted(s)
            key = ''
            for i in l: key += i

            if key in hmap:
                hmap[key].append(s)
            else:
                hmap[key] = [s]

        res = []

        for key in hmap:
            res.append(hmap[key])

        return res
                