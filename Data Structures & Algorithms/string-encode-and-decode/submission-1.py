class Solution:

    def encode(self, strs: List[str]) -> str:
        result = []

        for string in strs:
            result.append(str(len(string)) + '#' + string)
        print(result)
        return ''.join(result)


    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            cur_len = ''
            while s[i] != '#':
                cur_len += s[i]
                i += 1
            cur_len = int(cur_len)
            result.append(s[i + 1: i + 1 + cur_len])
            i += cur_len + 1          
        return result
