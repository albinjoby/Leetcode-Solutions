class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        original = [0]*len(derived)
        original[0] = 0
        for i in range(len(derived)-1):
            original[i+1] = original[i] ^ derived[i]
        original[-1] = original[0] ^ derived[-1]
        print(original)
        
        for i in range(len(derived)-1):
            if original[i] ^ original[i+1] != derived[i]:
                return False

        return original[-1] ^ original[0] == derived[-1]