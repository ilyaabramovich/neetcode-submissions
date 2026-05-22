class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        indices = sorted(range(len(position)), key = lambda x: -position[x])
        times = [(target - position[i]) / speed[i] for i in indices]
        stack = []
        for time in times:
            if not stack or stack[-1] < time:
                stack.append(time)
        return len(stack)