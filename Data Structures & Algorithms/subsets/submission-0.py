class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        self._subsets(nums,path,res,0)
        return res
    
    def _subsets(self, arr,path,res,i):
        if i == len(arr):
            res.append(path[:])
            return
        
        path.append(arr[i])
        self._subsets(arr,path,res,i+1)
        path.pop()


        self._subsets(arr,path,res,i+1)
        