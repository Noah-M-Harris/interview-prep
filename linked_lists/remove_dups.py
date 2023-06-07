"""
given a linked list of integers, remove all duplicate nodes
"""
from linked_list import LL, Node


def solution(root):
    # keeps track of all node values already seen
    buffer = set()
    dummy = Node(-1)
    prev = dummy

    # buffer keeps track of all the nodes already present in the new linked list
    curr = root
    while curr:
        if curr.val not in buffer:
            prev.next = Node(curr.val)
            buffer.add(curr.val)
            prev = prev.next
        curr = curr.next
    return dummy.next

root = Node(2)
linkedList = LL(root)
linkedList.add(34)
linkedList.add(4)
linkedList.add(3)
linkedList.add(23)
linkedList.add(34)
linkedList.add(1)
linkedList.add(37)
root = linkedList.root
print(solution(root))

