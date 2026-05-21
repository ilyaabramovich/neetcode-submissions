class Solution:

    def encode(self, strs: List[str]) -> str:
        return ''.join([str(len(string)) + '#' + string for string in strs])


    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            cur_len = ''
            while s[i] != '#':
                cur_len += s[i]
                i += 1
            start = i + 1
            end = start + int(cur_len)
            result.append(s[start: end])
            i = end          
        return result
