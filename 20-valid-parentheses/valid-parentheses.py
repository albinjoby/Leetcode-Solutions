class Solution:
    def isValid(self, s: str) -> bool:
        dic = {
            '}' : '{',
            ']' : '[',
            ')' : '('
        }
        stack = []
        for l in s:
            if l not in dic:
                stack.append(l)
            else:
                if stack and stack[-1] ==  dic[l]:
                    stack.pop()
                else:
                    return False
                
        return not stack