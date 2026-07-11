class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = set()
        i = 0
        ans = 0

        for j in range(len(s)):
            while s[j] in chars:
                chars.remove(s[i])
                i += 1
            ans = max(ans, j - i + 1)
            chars.add(s[j])
        
        return ans