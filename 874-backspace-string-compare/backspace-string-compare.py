class Solution(object):
    def check(self,s):
            stack = []
            for i in s:
                if i == '#' and not stack:
                    continue
                elif i =='#':
                    stack.pop(-1)
                else:
                    stack.append(i)

            return stack

    def backspaceCompare(self, s, t):
        return self.check(s)==self.check(t)
        