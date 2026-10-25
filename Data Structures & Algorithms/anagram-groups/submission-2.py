class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = {}
        ret = []
        for string in strs:
            key = "".join(sorted(string))
            hmap.setdefault(key, []).append(string)
        for key in hmap:
            ret.append(hmap[key])
        return ret