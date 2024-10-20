class Solution:
    def parseBoolExpr(self, s: str) -> bool:
        stack = []

        for c in s:
            if c != ')' and c != ',':
                stack.append(c)
            elif c == ')':
                lst = []

                while stack and stack[-1] != '(':
                    val = stack.pop()
                    lst.append(True if val == 't' else False)

                stack.pop()

                if stack:
                    exp = stack.pop()
                    x = lst[0]

                    if exp == '&':
                        for i in lst:
                            x &= i
                    elif exp == '|':
                        for i in lst:
                            x |= i
                    else:
                        x = not x

                    stack.append('t' if x else 'f')

        return stack[-1] == 't'