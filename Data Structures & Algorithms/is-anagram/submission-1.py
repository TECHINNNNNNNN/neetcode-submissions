class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count1 = {}
        count2 = {}
        for c in s:
            count1[c] = 1 + count1.get(c,0)
        for c in t:
            count2[c] = 1 + count2.get(c,0)
        

        count1 = dict(sorted(count1.items(), key=lambda item:item[1]))
        count2 = dict(sorted(count2.items(), key=lambda item:item[1]))

        print(count1)
        print(count2)

        if count1 == count2:
            return True
        
        return False
