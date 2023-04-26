# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # DIFFERENCE FROM OLD CODE
        # I implemented a dictionary keeping track of the level of each node
        # this being level_start
        # same principles follow of taking the distance of each of the node levels and then going through the tree with  
        # with BFS. 
        
        
        # Initialize the result and a queue for the tree nodes
        res = 0
        q = deque([(root, 0, 0)])
        level_start = {}
        
        # Loop through the queue
        while q:
            node, depth, pos = q.popleft()
            
            # Store the position of the leftmost node in each level
            if depth not in level_start:
                level_start[depth] = pos
            
            # Update the result with the maximum width of the current level
            res = max(res, pos - level_start[depth] + 1)
            
            # Add the child nodes to the queue
            if node.left:
                q.append((node.left, depth + 1, pos * 2))
            if node.right:
                q.append((node.right, depth + 1, pos * 2 + 1))
                
        return res

    # OLD CODE 
    from collections import deque

# class Solution:
#     def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
#         # Initialize the result and a queue for the tree nodes
#         res = 0
#         q = deque([(root, 0, 0)])
#         level_start = {}
        
#         # Loop through the queue
#         while q:
#             node, depth, pos = q.popleft()
            
#             # Store the position of the leftmost node in each level
#             if depth not in level_start:
#                 level_start[depth] = pos
            
#             # Update the result with the maximum width of the current level
#             res = max(res, pos - level_start[depth] + 1)
            
#             # Add the child nodes to the queue
#             if node.left:
#                 q.append((node.left, depth + 1, pos * 2))
#             if node.right:
#                 q.append((node.right, depth + 1, pos * 2 + 1))
                
#         return res

        