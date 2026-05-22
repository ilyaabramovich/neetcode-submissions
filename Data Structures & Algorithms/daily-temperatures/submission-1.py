class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [0]

        i = 1

        while i < len(temperatures):
            if len(stack) > 0 and temperatures[stack[-1]] < temperatures[i]:
                idx = stack.pop()
                res[idx] = i - idx
            else:
                stack.append(i)
                i += 1
        print(stack)
        return res
        