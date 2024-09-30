class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = [-1] * maxSize
        self.capacity = maxSize
        self.top = -1

    def push(self, x: int) -> None:
        # if self.top == -1:
        #     self.top += 1
        #     self.stack[top] = x
        if self.top + 1 < self.capacity:
            self.top += 1
            self.stack[self.top] = x

    def pop(self) -> int:
        if self.top == -1:
            return -1
        else:
            val = self.stack[self.top]
            self.top -= 1
            return val

    def increment(self, k: int, val: int) -> None:
        k = k if k < self.capacity else self.capacity

        for i in range(k):
            self.stack[i] += val

# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)