class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = {i: [] for i in range(n)}


        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        def dfs(node):
            visited.add(node)

            for n in graph[node]:
                if n not in visited:
                    dfs(n)

    
        visited = set()
        count = 0

        for node in range(n):
            if node not in visited:
                count += 1


                dfs(node)
        

        return count
                