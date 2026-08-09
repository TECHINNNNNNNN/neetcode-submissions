class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ''
        for w in strs:
            encoded += str(len(w))
            encoded += '|'
            encoded += w
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0
        while i < len(s):
            j = s.find('|',i)

            length = int(s[i:j])


            content = s[j + 1: j + 1 + length]
            decoded.append(content)
            i = j + 1 + length
        
        return decoded
