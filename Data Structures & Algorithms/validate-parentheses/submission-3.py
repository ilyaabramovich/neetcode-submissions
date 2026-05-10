class Solution:
    def isValid(self, s: str) -> bool:
        brackets = { ')': '(', ']': '[', '}': '{' }
        stack = []

        for c in s:
            if c in brackets:
                if len(stack) == 0 or brackets[c] != stack.pop():
                    return False
            else:
                stack.append(c)
        return len(stack) == 0