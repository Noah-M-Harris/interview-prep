"""
Given a linked list, swap every two adjacent nodes and return its head. 
You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)
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



def solution(head):
    """
    Input: head = [1,2,3,4]
    Output: [2,1,4,3]   

    Input: head = [1, 2, 3]
    Output: [2, 1, 3]

    consider even, odd cases
    """
    dummy = prev = Node(-1)
    curr = head

    while curr and curr.next:
        # save curr.next.next <- start of the next node pair
        nxtNode = curr.next.next

        # now swap curr and curr.next, be sure to fix the next node of both
        first, second = curr, curr.next
        prev.next = second
        second.next = first
        first.next = nxtNode

        # move prev up and move to nxtNode
        prev = first
        curr = nxtNode

    return dummy.next


root = Node(1)
second = Node(2)
third = Node(3)
fourth = Node(4)
root.next = second
second.next = third
third.next = fourth

print(solution(root)) # Output: [2,1,4,3]  


root = Node(1)
second = Node(2)
third = Node(3)
root.next = second
second.next = third

print(solution(root)) # Output: [2,1,3]  
