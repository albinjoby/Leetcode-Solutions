class Solution(object):
    def backspaceCompare(self, s, t):
        def check(s):
            result = []
            for i in s:
                if i != '#':
                    result.append(i)
                elif result:
                    result.pop()
                
            return ''.join(result)
        
        return check(s)==check(t)
        