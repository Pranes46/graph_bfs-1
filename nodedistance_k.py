# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:

        
        adj = defaultdict(list)
        
        q = deque([root])
        visited = set()
        
        while q:
            curr = q.popleft()
            
            if curr.left:
                adj[curr.left].append(curr)
                adj[curr].append(curr.left)
                q.append(curr.left)
                
            if curr.right:
                adj[curr.right].append(curr)
                adj[curr].append(curr.right)
                q.append(curr.right)
        
                
        q.append(target)
        
        while q and k>0:
            size = len(q)
            
            for _ in range(size):
                currNode = q.popleft()
                visited.add(currNode)
                
                for neighbors in adj[currNode]:
                    if neighbors not in visited:
                        
                        q.append(neighbors)
                    
                    
                    
            k-=1
            
        result = []
        
        for node in q:
            result.append(node.val)
            
        return result
                    
                
                
                
        
        