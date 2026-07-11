class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = {}
        i = 0
        ans = 0

        for j in range(len(s)):
            if s[j] in chars:
                idx = chars[s[j]]
                while i <= idx:
                    i += 1
            ans = max(ans, j - i + 1)
            chars[s[j]] = j
        
        return ans