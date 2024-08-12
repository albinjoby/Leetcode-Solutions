class Solution(object):
    def backspaceCompare(self, s, t):
        def check(s):
            stack = []
            for i in s:
                if i == '#' and not stack:
                    continue
                elif i =='#':
                    stack.pop(-1)
                else:
                    stack.append(i)

            return stack
        
        return True if check(s)==check(t) else False
        