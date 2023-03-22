# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # SOLUTION: Depth First Search
# Use a variable to track level in the tree and use simple Pre-Order traversal
# Add sub-lists to result as we move down the levels
# Time Complexity: O(N)
# Space Complexity: O(N) + O(h) for stack space
        
        
        
        # STEP ONE: create a result variable and establish a helper function 
        result = []
        self.helper(root,0,result)
        return result
    
    def helper(self, root, level, result):
        # if there is no root value prevalent. 
        if root is None:
            return 
        # if the len of the result is less than the level of the subtree, add an empty list.
        if len(result) <= level:
            result.append([])
         
        
        result[level].append(root.val)
        self.helper(root.left, level+1, result)
        self.helper(root.right, level+1, result)
            
        
        
       
            
            
           
                    
        
        
        
        
       