class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        di = {}

        for ch in strs:
            k = tuple(sorted(ch))
            di.setdefault(k, [])
            di[k].append(ch)

        return list(di.values())