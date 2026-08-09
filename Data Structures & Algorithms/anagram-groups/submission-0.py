class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return []
        store = {}
        res = []

        for w in strs:
            if tuple(sorted(w)) not in store:
                store[tuple(sorted(w))] = []
            store[tuple(sorted(w))].append(w)
        
        for v in store.values():
            res.append(v)
        
        return res
        