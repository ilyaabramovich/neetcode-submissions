class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n
        stack = []

        for curr_idx, curr_temp in enumerate(temperatures):
            # Пока текущая температура выше той, что в стеке
            while stack and temperatures[stack[-1]] < curr_temp:
                prev_idx = stack.pop()
                res[prev_idx] = curr_idx - prev_idx
            
            # В любом случае добавляем текущий индекс в стек
            stack.append(curr_idx)
            
        return res