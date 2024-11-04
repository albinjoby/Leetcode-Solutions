class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for letter in s:
            if letter != ']':
                stack.append(letter)
            else:
                val = ''
                while stack[-1] != '[':
                    val = stack.pop() +  val
                stack.pop()
                num = ''
                while stack and stack[-1] in '1234567890':
                    num = stack.pop() + num
                count = int(num)
                res = ''
                for i in range(int(count)):
                    res += val
                stack.append(res)

        return ''.join(stack)