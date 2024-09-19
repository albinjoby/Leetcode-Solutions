class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operands = '+-*/'
        
        for symbol in tokens:
            if symbol in operands:
                num1 = stack.pop()
                num2 = stack.pop()
                if symbol == '+':
                    stack.append(num2 + num1)
                elif symbol == '-':
                    stack.append(num2 - num1)
                elif symbol == '*':
                    stack.append(num2 * num1)
                elif symbol == '/':
                    stack.append(int(num2 / num1))
            else:
                stack.append(int(symbol))
        
        return stack[0]