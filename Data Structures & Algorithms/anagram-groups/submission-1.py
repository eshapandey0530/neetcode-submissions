class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 'act' - ['act', 'cat']
        # the things that i need to keep in mind
        # the time complexity will be

        # time O(n * klog k)
        # space O(n*k)
        # k here being the length of each string in the array

        # strHashmap = {}

        # for s in strs:
        #     key = "".join(sorted(s))
        #     if key in strHashmap:
        #         strHashmap[key].append(s)
        #     else:
        #         strHashmap[key] = [s]

        # res = []

        # for value in strHashmap.values():
        #     res.append(value)

        # return res

        # time O(n * k)
        # space O(n*k)

        strHashmap = {}

        for string in strs:

            char = [0] * 26

            for s in string:

                index = ord(s) - ord('a')
                char[index] += 1

            key = tuple(char)

            if key in strHashmap:
                strHashmap[key].append(string)
            else:
                strHashmap[key] = [string]

        result = []

        for values in strHashmap.values():
            result.append(values)

        return result


