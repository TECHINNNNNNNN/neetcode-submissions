class Solution:
    def minWindow(self, s: str, t: str) -> str:
        window = {}
        left = 0
        right = 0
        store = {} # {right - left: [left, right]}
        formed = 0

        t_counter = {}
        for c in t:
            if c not in t_counter:
                t_counter[c] = 0
            t_counter[c] += 1
        

        while right < len(s):
            if s[right] not in window:
                window[s[right]] = 0
            window[s[right]] += 1
            if s[right] in t_counter and window[s[right]] == t_counter[s[right]]:
                formed += 1

            while formed == len(t_counter):
                store[right - left] = [left,right + 1]
                window[s[left]] -= 1
                if s[left] in t_counter and window[s[left]] < t_counter[s[left]]:
                    formed -= 1
                left += 1
            
            right += 1
        
        if len(store) == 0:
            return ""
        
        min_key = min(store)
        min_range = store[min_key]
        start = min_range[0]
        end = min_range[1]
        return s[start:end]
    
    def check(self,window, t_counter):
        for char,count in t_counter.items():
            if window.get(char,0) < count:
                return False
        
        return True

        