"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        
        time: O(n)
        space: O(1) 
        """
        if not head:
            return None

        # for each original node follow 1 copy node
        # A -> A' -> B -> B'
        curr = head
        while curr:
            # create a copy
            copy_node = Node(curr.val)
            # let copy connect with next node
            copy_node.next = curr.next
            # copy node follow the orginal node
            curr.next = copy_node
            # curr need to jump 2 step to next original node
            curr = curr.next.next

        curr = head
        while curr:
            if curr.random:
                #original points to whom, the clone points to that person's clone
                # curr.next is the copy
                curr.next.random = curr.random.next
            else:
                curr.next.random = None

            curr = curr.next.next

        # split A-A'-B-B' into 2 dependent linked list, A-B and A'-B'
        # original head
        curr_old = head
        # new head
        new_head = head.next
        curr_new = new_head

        while curr_old:
            # original list
            curr_old.next = curr_old.next.next

            # new list
            if curr_new.next:
                curr_new.next = curr_new.next.next
            else:
                curr_new.next = None

            curr_old = curr_old.next
            curr_new = curr_new.next

        return new_head


            
        