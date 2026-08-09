class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        L = 0
        count = 0
        current_sum = 0

        for R in range(len(arr)):
            current_sum += arr[R]
            if R - L + 1 > k:
                current_sum -= arr[L]
                L += 1
            
            if R - L + 1 == k and current_sum / (R - L + 1) >= threshold:
                count += 1
        
        return count


        