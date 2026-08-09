class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return []
        store = {}
        res = []

        for w in strs:
            wordKey = tuple(self.arrayKey(w))
            if wordKey not in store:
                store[wordKey] = []
            store[wordKey].append(w)
        
        for v in store.values():
            res.append(v)
        
        return res
        
    def arrayKey(self,s):
        count_array = [0] * 26
        for char in s:
            index = ord(char) - ord('a')
            count_array[index] += 1
        
        return count_array
