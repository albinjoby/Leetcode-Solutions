class Solution:
    def isValid(self, s: str) -> bool:
        dic = {
            ']' : '[',
            '}' : '{',
            ')' : '('
        }
        stack = []
        for letter in s:
            if letter in dic and stack and dic[letter] == stack[-1]:
                stack.pop()
            else:
                stack.append(letter)

            
        return len(stack) == 0
