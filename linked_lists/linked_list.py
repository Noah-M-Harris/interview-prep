class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        result = ""
        result += ", " + str(self.val)
        curr = self.next
        while curr:
            result += ", " + str(curr.val)
            curr = curr.next

        return "[" + result.strip(", ") + "]"

    def add(self, node):
        # adds a node to the end of a linkedlist starting at this position
        if not isinstance(node, Node):
            node = Node(node)

        if not self.next:
            self.next = node
            return True
        
        curr = self.next
        while curr and curr.next:
            curr = curr.next
        curr.next = node
        return True


class LL:
    def __init__(self, root=None):
        self.root = root
        self.pos = root

    def add(self, node):
        
        if not isinstance(node, Node):
            node = Node(node)

        self.pos.next = node
        self.pos = self.pos.next
    
    def __repr__(self):
        curr = self.root
        result = ""
        while curr:
            result += str(curr.val) + " "
            curr = curr.next
        return result

"""
root = Node(-1)
linkedList = LL(root)
linkedList.add(2)
node = Node(3)
linkedList.add(node)
# print(repr(linkedList))
# print(str(linkedList))
print(linkedList)
"""

root = Node(-1)
second = Node(0)
third = Node(1)
root.next = second
second.next = third
third.next = Node(2)
print(root.next)
