class TreeNode:
    def __init__(self, val, right=None, left=None):
        self.data = val
        self.right = right
        self.left = left

class BST:
    def __init__(self, root):
        if not isinstance(root, TreeNode):
            self.root = TreeNode(root)
        else:
            self.root = root
    
    def insert(self, val):
        return self._insert(val, self.root)
    
    def _insert(self, val, root):
        if not root:
            return TreeNode(val)
        if val < root.data:
            root.left = self._insert(val, root.left)
        else:
            root.right = self._insert(val, root.right)
        return root

    def remove(self, val):
        """ remove the given val if it is present within the tree """
        """ consider the case where root has either 0 or 1 children or no children """
        return self._remove(val, self.root)
    
    def _remove(self, val, root):
        """ first try to locate val """
        if not root:
            return None

        if val < root.data:
            return self._remove(val, root.left)
        elif val > root.data:
            return self._remove(val, root.right)
        else:
            # we located val, consider the two cases
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                # both children present, find in order successor, left most node in the right tree
                inorder_successor = self.findMin(root.right)
                root.data = inorder_successor.data
                root.right = self._remove(inorder_successor.val, root.right)
        return root

    def findMin(self, root):
        curr = root
        while curr and curr.left:
            curr = curr.left
        return curr

    """
    inorder: left, root, right
    preorder: root, left, right
    postorder: left, right, root
    """

    def inorder_print(self):
        self._inorder_print(self, self.root)
    
    def _inorder_print(self, root):

        if not root:
            return 

        self._inorder_print(root.left)
        print(root.data)
        self._inorder_print(root.right)

    def preorder_print(self):
        self._preorder_print(self, self.root)

    def _preorder_print(self, root):
        
        if not root:
            return
        
        print(root.data)
        self._preorder_print(root.left)
        self._preorder_print(root.right)

    def postorder_print(self):
        self._preorder_print(self, self.root)

    def _postorder_print(self, root):
        
        if not root:
            return
        
        self._preorder_print(root.left)
        self._preorder_print(root.right)
        print(root.data)


