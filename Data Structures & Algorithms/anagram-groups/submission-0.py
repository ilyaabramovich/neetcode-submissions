from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for word in strs:
            arr = [0] * 26
            for c in word:
                arr[ord(c) - ord('a')] += 1
            d[tuple(arr)].append(word)
        return list(d.values())
        