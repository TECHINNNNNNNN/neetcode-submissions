class UnionFind:
    def __init__(self,n):
        self.par = {}
        self.rank = {}

        for i in range(n):
            self.par[i] = i
            self.rank[i] = 0
    
    def find(self, n):
        p = self.par[n]
        while p != self.par[p]:
            self.par[p] = self.par[self.par[p]]
            p = self.par[p]
        
        return p
    
    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)

        if p1 == p2:
            return False
        
        if self.rank[p1] < self.rank[p2]:
            self.par[p1] = p2
        elif self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1 
        else:
            self.par[p1] = p2
            self.rank[p2] += 1
        
        return True


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        emailMap = {}
        graph = UnionFind(len(accounts))

        for i, acc in enumerate(accounts):
            for email in acc[1:]:
                if email not in emailMap:
                    emailMap[email] = i
                else:
                    graph.union(i , emailMap[email])

        mergedAccounts = {}

        for k, v in emailMap.items():
            parent = graph.find(v)
            if parent not in mergedAccounts:
                mergedAccounts[parent] = []
            mergedAccounts[parent].append(k)
        
        result = []
        for k, v in mergedAccounts.items():
            name = accounts[k][0]
            tmp = [name]
            tmp += sorted(v)
            
            result.append(tmp)
        
        return result





        
