class Solution:
    def reverseBits(self, n: int) -> int:
        reversedNumber = []
        while n:
            if n & 1 == 1:
                reversedNumber.append(1)
            else :
                reversedNumber.append(0)
            
            n = n >> 1
        
        while len(reversedNumber) <= 32:
            reversedNumber.append(0)

        result = 0
        print(reversedNumber)
        for i in range(32):
            result += reversedNumber[i] * (2 ** (32 - (i + 1)))
        
        return result