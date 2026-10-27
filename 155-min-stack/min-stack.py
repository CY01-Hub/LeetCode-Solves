class MinStack:

    def __init__(self):
        self.mainStack = []
        self.minStack = []

    def push(self, value: int) -> None:
        self.mainStack.append(value)

        if len(self.minStack) == 0 or value <= self.minStack[-1]:
            self.minStack.append(value)

    def pop(self) -> None:
        x = self.mainStack.pop()

        if x == self.minStack[-1]:
            self.minStack.pop()

    def top(self) -> int:
        return self.mainStack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()