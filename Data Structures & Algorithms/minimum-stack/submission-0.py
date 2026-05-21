class MinStack:

    def __init__(self):
        self.elements = []
        self.prefix_min = []
        self.min_val = float('inf')

    def push(self, val: int) -> None:
        self.elements.append(val)
        val = min(val, self.prefix_min[-1] if self.prefix_min else val)
        self.prefix_min.append(val)

    def pop(self) -> None:
        self.elements.pop()
        self.prefix_min.pop()
        

    def top(self) -> int:
        return self.elements[-1]

        

    def getMin(self) -> int:
        return self.prefix_min[-1]
        
