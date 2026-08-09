class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left = 0
        right = 0
        min_range = float('inf')
        store = {}

        while right < len(s):
            right += 1
            while self.isValid(s[left:right],t):
                min_range = min(min_range, right - left)
                store[right - left] = [left,right]
                left += 1
        
        if len(store) == 0:
            return ""
        
        min_value = store[min(store)]
        start = min_value[0]
        end = min_value[1]
        return s[start:end]
        


    
    def isValid(self,arr, t):
        t_counter = {}
        tmp = {}
        for c in t:
            if c not in t_counter:
                t_counter[c] = 0
            t_counter[c] += 1
        
        for c in arr:
            if c not in tmp:
                tmp[c] = 0
            tmp[c] += 1
        
        for char, count in t_counter.items():
            if tmp.get(char,0) < count:
                return False
        
        return True

        