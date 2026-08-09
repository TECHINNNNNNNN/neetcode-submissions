class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        graph = {i:[] for i in range(n)}
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
        visited = set()


        

        def dfs(node,parent):
            visited.add(node)

            for n in graph[node]:
                if n == parent:
                    continue
            
                if n in visited:
                    return False

                if not dfs(n,node):
                    return False
            
            return True
        
        if not dfs(0,-1):
            return False
        
        return len(visited) == n
                
        
