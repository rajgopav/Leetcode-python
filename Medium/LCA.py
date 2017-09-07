class TreeNode():
    def __init__(self, x):
        self.value = x
        self.left = None
        self.right = None

class Solution():
    def LCA(self, root, p, q):
        s, b = sorted([p.value, q.value])
        while not s <= root.value <= b:
            root = root.left if s <= root.value else root.right
        return root

if __name__ == '__main__':
    root = TreeNode(6)
    root.left = TreeNode(2)
    root.right = TreeNode(8)
    root.left.left = TreeNode(0)
    root.left.right = TreeNode(4)
    root.left.right.left = TreeNode(3)
    root.left.right.right = TreeNode(5)
    root.right.left = TreeNode(7)
    root.right.right = TreeNode(9)
    print Solution().LCA(root, root.left, root.right).value