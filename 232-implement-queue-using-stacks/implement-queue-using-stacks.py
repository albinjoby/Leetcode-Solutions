class MyQueue:

    def __init__(self):
        self.stack = []
        self.temp = []
        self.front = 0
        return

    def push(self, x: int) -> None:
        self.stack.append(x)
        return

    def pop(self) -> int:
        val = self.stack[self.front]
        self.stack[self.front] = -1
        self.front += 1
        return val

    def peek(self) -> int:
        return self.stack[self.front]
        
    def empty(self) -> bool:
        count = 0
        for num in self.stack:
            if num != -1:
                count += 1
        return count == 0

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()