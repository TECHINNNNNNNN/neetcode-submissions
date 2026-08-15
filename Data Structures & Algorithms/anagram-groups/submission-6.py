class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        tmpDict = defaultdict(list)


        for word in strs:
            count = [0] * 26

            for c in word:
                count[ord('a') - ord(c)] += 1
            

            tmpDict[tuple(count)].append(word)
        
        return [v for k,v in tmpDict.items()]
            
        