class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        dic = {chr(x): x - 48 for x in range(48,58)}
        def get_num(s:str) -> int:
            val = 0
            for c in s:
                val *= 10
                val += dic[c]
            return val
        return str(get_num(num1) * get_num(num2))