class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        left = 0
        max_length = 0
        for right in range(len(s)):
            count[s[right]] = count.get(s[right],0) + 1
            max_freq = max(count.values()) if count else 0

            window_length = right - left + 1
            replacement_needed = window_length - max_freq

            while replacement_needed > k:
                if count[s[left]]:
                    count[s[left]] -= 1
                left += 1
                max_freq = max(count.values()) if count else 0
                window_length = right - left + 1
                replacement_needed = window_length - max_freq
            

            max_length = max(max_length, right - left + 1)
        
        return max_length

