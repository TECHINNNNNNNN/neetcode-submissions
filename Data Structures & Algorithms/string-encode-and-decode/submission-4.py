class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for word in strs:
            result += str(len(word))
            result += '@'
            result += word
        print(result)
        return result

    def decode(self, s: str) -> List[str]:
        decoded = []
        word = ''
        i = 0
        while i < len(s):
            numberString = ''
            while i < len(s) and s[i] != '@':
                numberString += s[i]
                i += 1
            lengthOfWord = int(numberString)
            i += 1
            word += s[i: i + lengthOfWord]
            decoded.append(word)
            word = ''
            i = i + lengthOfWord
        
        return decoded
            

            

