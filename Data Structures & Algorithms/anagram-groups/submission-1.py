class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for i in strs:
            SortedStrs = ''.join(sorted(i))
            result[SortedStrs].append(i)
        return list(result.values())
        