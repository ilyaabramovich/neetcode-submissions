class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        res = 1
        indices = sorted(range(len(position)), key = lambda x: -position[x])
        times = [(target - position[i]) / speed[i] for i in indices]
        stack = [times[0]]
        for i in range(1, len(times)):
            if stack[-1] < times[i]:
                res += 1
                stack.append(times[i])
        print(times)
        return res