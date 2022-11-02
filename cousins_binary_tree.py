# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:  #tc - o(n(. sc - o(n)
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        
        q = deque()  #initailiazing the queue using deque
        q.append(root)  #appending the root into the queue
        
        while q:  #until the q is empty the loop will run
            size = len(q)  #we are doing level order traversal so we need size parameter
            level = set()  #to append the node value which we visited
            
            for i in range(size):  #level order traversal
                node = q.popleft()  #popping the first element from the queu and storing it in a variable
                level.add(node.val)  #adding the popped node value into the level set
                
                if node.left and node.right and ((node.left.val ==x and node.right.val ==y) or (node.left.val==y and node.right.val == x)):
                    
                    return False  #if the node's left and right child is x and y or y and x means they are not cousin so we are returning it
                    
                if node.left:  #appending the left child of the node
                    q.append(node.left)

                    
                if node.right:   #appending the right of the node
                    q.append(node.right)
                    
                    
            if x in level and y in level:  #if the x and y are in level set we are returning true
                return True
            
        return False
