class Solution(object):
    def findComplement(self, num):
        binary = bin(num)[2:]
        complement = ''
        for bit in binary:
            complement += str(int(bit)^1)
        complement = int(complement,2)
        return complement