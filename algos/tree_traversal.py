class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def preorder(root: TreeNode):
    return [root.val] + preorder(root.left) + preorder(root.right) if root else []


def inorder(root: TreeNode):
    return inorder(root.left) + [root.val] + inorder(root.right) if root else []


def postorder(root: TreeNode):
    return postorder(root.left) + postorder(root.right) + [root.val] if root else []
