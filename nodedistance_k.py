# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:  #tc - o(n(. sc - o(n)
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:

        
        adj = defaultdict(list). #adj list 
        
        q = deque([root]). #appending the root in the queue, we are using bfs here
        visited = set() #we are creating a hashset to store the visited node
        
        while q:  #the loop will run until there is a value in queue
            curr = q.popleft() #popping the first element in the queue
            
            if curr.left:  #if the popped node has left child we are appending it in the queue and we are storing the popped element as key and the left child as value in adj list
                adj[curr.left].append(curr)
                adj[curr].append(curr.left)
                q.append(curr.left)
                
            if curr.right: #if the popped node has right child we are appending it in the queue and we are storing the popped element as key and the right child as value in adj list
                adj[curr.right].append(curr)
                adj[curr].append(curr.right)
                q.append(curr.right)
        
                
        q.append(target). #appending the target in the queue
        
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
                    
                
                
                
        
        
