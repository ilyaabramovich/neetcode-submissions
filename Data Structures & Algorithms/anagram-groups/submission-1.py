class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for word in strs:
            arr = [0] * 26
            for c in word:
                arr[ord(c) - ord('a')] += 1
            key = tuple(arr)
            if key in d:
                d[key].append(word)
            else:
                d[key] = [word]
        return list(d.values())
        