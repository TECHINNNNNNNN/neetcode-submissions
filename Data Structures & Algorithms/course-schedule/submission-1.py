class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {i : [] for i in range(numCourses)}

        for a,b in prerequisites:
            adj[a].append(b)
        
        def dfs(node,path):
            if node in path:
                return False
            path.add(node)

            for nei in adj[node]:
                if not dfs(nei,path):
                    return False
            path.remove(node)
            return True

        for i in range(len(prerequisites)):
            if not dfs(prerequisites[i][0],set()):
                return False
        return True
        



        