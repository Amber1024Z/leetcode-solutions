"""
LRU = Least Recently Used

When the cache is full, delete the data that has not been used for the longest time to make room for new data

Since required O(1) time complexity for get and put, we can use a hash map to store the key and value, and a double linked list to store the order of usage. 
The most recently used data will be moved to the head of the list, and the least recently used data will be at the tail of the list. When we need to delete the least recently used data, we can simply remove the tail node of the list.
"""

class Node:
    # prev ← [ key | val ] → next
    def __init__(self, key):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache(object):

    def __init__(self, capacity):
        # dict (key → node)  +  doubly linked list
        # head <-> node1 <-> node2 <-> node3 <-> tail
        # head and tail are dummy nodes
        self.capacity = capacity
        self.cache = {}
        self.head = Node()
        self.tail = Node()
        self.head.next = tail
        self.tail.prev = head

    def remove_node(self, node):
        # Permanently remove a node from the linked list
        node.prev.next = node.next
        node.next.prev = node.prev

    def add_to_head(self, node):
        # move node to head, means recently used
        node.next = self.head.next
        node.prev = self.head
        # head ⇄ node ⇄ A ⇄ B ⇄ tail
        self.head.next.prev = node 
        self.head.next = node 

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.cache:
            return -1 
        node = self.cache[key]
        # if exsits, move to head means recently used
        self.remove_node(node)
        self.add_to_head(node)
        return node.value

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.cache:
            # when key exsits, update value and move to head
            node = self.cache[key]
            node.value = value
            self.remove_node(node)
            self.add_to_head(node)
        else:
            new_node = Node(key, value)
            self.cache[key] = new_node
            self.add_to_head(new_node)

            # if exceed capacity, remove tail
            if len(self.cache) > len(self.capacity):
                need_move_node = self.tail.prev
                self.remove_node(need_move_node)
                # also need to remove this node from dict
                del self.cache[need_move_node.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
