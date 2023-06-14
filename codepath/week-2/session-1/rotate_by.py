"""
Given the head of a linked list, rotate the list to the right by k places.

Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]
"""


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



def solution(head, k):
    """ count the length of the linked list """
    """ while length - processed node != k, we continually move nodes to the end of the linked list """
    dummy = prev = Node(-1, head)
    length = 0
    
    curr = head
    while curr:
        length += 1
        prev, curr = prev.next, curr.next
    
    end = prev
    curr, prev = head, dummy
    processed = 0

    while length - processed != k:
        curr, prev = curr.next, prev.next
        processed += 1
    
    prev.next = None
    # curr is the new head
    end.next = head
    dummy.next = curr
    return curr
    

    """
    while length - processed < (k - 1):
        curr, prev = curr.next, prev.next
        processed += 1

    # move the head of linkedlist to prev.next
    prev.next = None
    end.next = head
    return curr
    """


root = Node(1)
second = Node(2)
third = Node(3)
fourth = Node(4)
fifth = Node(5)
root.next = second
second.next = third
third.next = fourth
fourth.next = fifth

print(solution(root, 2)) # Output: [4,5,1,2,3]


root = Node(1)
second = Node(2)
third = Node(3)
fourth = Node(4)
root.next = second
second.next = third
third.next = fourth

print(solution(root, 3)) # Output: [2,3,4,1]