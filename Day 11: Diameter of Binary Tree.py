# Diameter of Binary Tree
#
# Given a binary tree, you need to compute the length of the diameter of the tree.
# The diameter of a binary tree is the length of the longest path between any two
# nodes in a tree. This path may or may not pass through the root.
#
# Note: The length of path between two nodes is represented by the number of edges between them.
#
# The diameter of a tree is the number of nodes on the longest path between two end nodes.

# Definition for a binary tree node.
#class TreeNode(object):
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None


class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def heightOfTree(root):
            if not root:
                return 0
            # Return a hight of binary tree  
            return 1 + max(heightOfTree(root.left), heightOfTree(root.right))

        
        if not root:
            return 0
        left_height = heightOfTree(root.left)
        reight_height = heightOfTree(root.right)

        # Get diameter left and right sub-trees
        left_diameter = self.diameterOfBinaryTree(root.left)
        right_diameter = self.diameterOfBinaryTree(root.right)
        
        # Get max path between leaves which passe through root
        return max((left_height + reight_height), max(left_diameter, right_diameter))
    
    
