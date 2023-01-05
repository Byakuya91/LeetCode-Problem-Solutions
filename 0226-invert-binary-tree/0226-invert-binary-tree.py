# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        
        
        # POA
        # 1) Research what a tree is in programming(DONE)
        # 2) Research DFS algorithm and incorporate it(DONE)
        # 3) Brush up on recursion to be utilized(DONE)
       
       # STEP ONE: define a base case
        if not root:
            return None 
        
        # STEP TWO: swap the children of the BT
        temp = root.left
        root.left = root.right
        root.right =temp
        
        # STEP THREE recursive calls on the leftmost truee and rightmost trees
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        # STEP FOUR: return the root of the tree
        return root
        
        
    
       
        