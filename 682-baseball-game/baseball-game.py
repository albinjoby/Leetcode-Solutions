class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for operation in operations:
            if operation == 'C':
                stack.pop()
            elif operation == 'D':
                val = stack[-1]*2
                stack.append(val)
            elif operation == '+':
                a = stack[-1]
                b = stack[-2]
                stack.append(a+b)
            else:
                stack.append(int(operation))

        return sum(stack)
