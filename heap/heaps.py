

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




class MinHeap:
    def __init__(self, maxsize=None):
        self.heap = [-1]
        self.size = maxsize

    def insert(self, val):
        if self.size is not None and (len(self.heap) - 1) >= self.size:
            raise KeyError("Length of heap will be excedded")
        
        """ insert val at the end of heap, move it up """
        self.heap.append(val)
        self.size += 1

        return self._heapify_up(len(self.heap)-1)

    def _heapify_up(self, pos):
        """ find the parent, check if the val @ this position is less than parent, if so swap, heapify up """
        if pos == 1:
            return True
        
        parent_idx = pos // 2
        parent, child = self.heap[parent_idx], self.heap[pos]

        if child < parent:
            # swap positions
            self.heap[parent_idx], self.heap[pos] = child, parent
            self._heapify_up(parent_idx)
        return True

    def pop(self):
        """ replace the top element with the last element and heapify down the last element """
        if len(self.heap) <= 1:
            return False

        self.heap[1], self.heap[-1] = self.heap[-1], self.heap[1]
        top = self.heap.pop()
        self.size -= 1

        self._heapify_down(self, 1)
        return top

    def _heapify_down(self, pos):
        """ heapify down the top element """

        # left child is out of bounds
        if (pos * 2) >= len(self.heap):
            return
        
        # left_i, right_i = self.heap[pos * 2], self.heap[pos * 2 + 1]

        """ swap with the min element out of the two children """
        """ concluded left child exists, make sure right does as well """
        left_i = pos * 2

        if (pos * 2 + 1) >= len(self.heap):
           """ only potential swap is with left child """
           if self.heap[pos] > self.heap[left_i]:
                self.heap[pos], self.heap[left_i] = self.heap[left_i], self.heap[pos]
                self._heapify_down(left_i)
        else:
            """ right child exists as well """
            """ check min between left and right and swap """
            right_i = pos * 2 + 1
            if self.heap[right_i] < self.heap[left_i]:
                self.heap[pos], self.heap[right_i] = self.heap[right_i], self.heap[pos]
                self._heapify_down(right_i)
            else:
                self.heap[pos], self.heap[left_i] = self.heap[left_i], self.heap[pos]
                self._heapify_down(left_i)
            