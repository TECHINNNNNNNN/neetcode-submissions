class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        path = []
        self._combinationSum(nums,path,0,0,target,res)
        return res
    
    def _combinationSum(self,arr,path,i,total,target,res):
        if i == len(arr) or total > target:
            return
        
        print(f"path = {path}")
        
        if total == target:
            res.append(path[:])
            return
        
        path.append(arr[i])
        total += arr[i]
        self._combinationSum(arr,path,i,total,target,res)
        path.pop()
        total -= arr[i]
        self._combinationSum(arr,path,i+1,total,target,res)
        
        