class Solution:
    def convertToBase7(self, num: int) -> str:
        res = ''
        if num > 0:
            while num != 0:
                rem = str(num % 7)
                res += rem
                num //= 7
            return res[::-1]
        elif num == 0:
            return '0'
        else:
            num = -num
            while num != 0:
                rem = str(num % 7)
                res += rem
                num //= 7
            return '-'+res[::-1]