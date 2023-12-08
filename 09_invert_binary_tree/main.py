from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def from_list(self, input_list):
        # make tree from list
        # use bfs
        queue = [self]
        for i in range(len(input_list)):
            node = queue.pop(0)
            node.val = input_list[i]
            if i * 2 + 1 < len(input_list):
                node.left = TreeNode()
                queue.append(node.left)
            if i * 2 + 2 < len(input_list):
                node.right = TreeNode()
                queue.append(node.right)

    def to_list(self):
        # make list from tree
        # use bfs
        queue = [self]
        result = []
        while queue:
            node = queue.pop(0)
            result.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return result
    


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: # base case if leaf
            return root

        # recursive left tree and right tree
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        # swap the left and right
        root.left, root.right = root.right, root.left

        return root
    
    def invertTree_iterative(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        
        queue = [root]
        while queue:
            node = queue.pop(0)
            node.left, node.right = node.right, node.left
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            
        return root
    
# test case
if __name__ == "__main__":
    sol = Solution()
    # make treenode from list
    input_list = [4,2,7,1,3,6,9]
    root = TreeNode().from_list(input_list)

    # print the result as a list
    invert_tree = sol.invertTree(root)
    print(root.to_list())
