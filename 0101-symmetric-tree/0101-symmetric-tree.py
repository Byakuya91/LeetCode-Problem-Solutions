# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # STEP ONE: create a function to intiate Depth-First-Search(DFS)
        def dfs(left,right):
            # Creating a base case
            if not left and not right:
                return True 
            # checking if both of the nodes are NOT null
            if not left or not right:
                return False 
            # Boolean checks to make sure the nodes are symmetric in the right left tree and left right tree and vice versa
            return (left.val == right.val and 
                   dfs(left.left,right.right) and 
                   dfs(left.right,right.left))
        
        # call the function
        return dfs(root.left,root.right)  
        
        
        
        
        
        
        # Understand the problem(ONGOING)
        #) research Binary trees and recursive calls
        
        