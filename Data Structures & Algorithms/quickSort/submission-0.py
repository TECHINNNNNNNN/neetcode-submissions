# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        e = len(pairs) - 1
        s = 0

        return self.quickSortHelp(pairs,s, e)


    
    def quickSortHelp(self, arr, s, e):
        if e - s + 1 <= 1:
            return arr
        
        pivot = arr[e]
        left = s

        for i in range(s,e):
            if arr[i].key < pivot.key:
                tmp = arr[left]
                arr[left] = arr[i]
                arr[i] = tmp
                left += 1
        
        arr[e] = arr[left]
        arr[left] = pivot

        self.quickSortHelp(arr,s, left - 1)
        self.quickSortHelp(arr, left + 1, e)

        return arr

        