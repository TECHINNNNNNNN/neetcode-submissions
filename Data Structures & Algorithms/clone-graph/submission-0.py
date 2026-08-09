"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        queue = deque([node])
        new_head = Node(node.val)
        clone_map = {node: new_head}

        while queue:
            current_original = queue.popleft()

            for original_neighbor in current_original.neighbors:
                if original_neighbor not in clone_map:
                    new_copy = Node(original_neighbor.val)
                    clone_map[original_neighbor] = new_copy
                    queue.append(original_neighbor)
                clone_map[current_original].neighbors.append(clone_map[original_neighbor])
            

        return new_head

        