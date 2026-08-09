class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def isEnough(n, arr, h):
            total = 0
            for i in range(len(arr)):
                total += -(-arr[i] // n)
            return total <=  h

        sumOfAllBananas = sum(piles)
        L = 1
        R = sumOfAllBananas

        while L < R:
            mid = L + (R - L) // 2
            print("L: ",L)
            print("R: ", R)
            print("isEnough: ",isEnough(mid, piles, h))
            if isEnough(mid, piles, h):
                R = mid
            else:
                L = mid + 1
        
        return L

        