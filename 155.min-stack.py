
class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append((val, val))
        else:
            (_, min_val) = self.stack[-1]
            if val < min_val:
                min_val = val
            self.stack.append((val, min_val))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        (val, _) = self.stack[-1]
        return val

    def getMin(self) -> int:
        (_, min_val) = self.stack[-1]
        return min_val


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
