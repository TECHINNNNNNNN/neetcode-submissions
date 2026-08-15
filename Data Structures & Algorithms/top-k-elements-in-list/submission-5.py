class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # [0,0,0,0,0,0]
        tmpDict = {}
        result = []
        freqList = [[] for _ in range(len(nums) + 1)]
        for num in nums:
            if num not in tmpDict:
                tmpDict[num] = 0
            tmpDict[num] += 1
        
        for numKey in tmpDict:
            freq = tmpDict[numKey]
            freqList[freq].append(numKey) 
        

        for elementList in freqList[::-1]:
            for n in elementList:
                result.append(n)
                if len(result) == k:
                    return result
        
        return 

        


        