# really hard WTH
class Node:
    def __init__(self, key, val):
        # Each node stores key + value
        self.key = key
        self.val = val
        
        # Pointers for doubly linked list
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        # Maximum capacity of cache
        self.cap = capacity
        
        # HashMap: key -> node (for O(1) access)
        self.cache = {}

        # Create dummy left (LRU) and right (MRU) nodes
        self.left = Node(0, 0)   # Least Recently Used
        self.right = Node(0, 0)  # Most Recently Used
        
        # Connect dummy nodes
        self.left.next = self.right
        self.right.prev = self.left


    # ---------------- HELPER FUNCTIONS ---------------- #

    def remove(self, node):
        """
        Remove a node from the doubly linked list
        """
        prev = node.prev
        nxt = node.next
        
        # Bypass the node
        prev.next = nxt
        nxt.prev = prev


    def insert(self, node):
        """
        Insert node at the right (MRU position)
        """
        prev = self.right.prev
        nxt = self.right
        
        # Insert node between prev and right
        prev.next = node
        node.prev = prev
        
        node.next = nxt
        nxt.prev = node


    # ---------------- MAIN OPERATIONS ---------------- #

    def get(self, key: int) -> int:
        """
        Return value of key if exists, else -1
        Also move the node to MRU position
        """
        if key in self.cache:
            node = self.cache[key]
            
            # Move accessed node to MRU (right)
            self.remove(node)
            self.insert(node)
            
            return node.val
        
        return -1


    def put(self, key: int, value: int) -> None:
        """
        Insert or update key-value pair
        If capacity exceeded → remove LRU
        """
        
        # If key already exists → remove old node
        if key in self.cache:
            self.remove(self.cache[key])
        
        # Create new node
        node = Node(key, value)
        
        # Add to hashmap
        self.cache[key] = node
        
        # Insert at MRU position
        self.insert(node)

        # If capacity exceeded → remove LRU node
        if len(self.cache) > self.cap:
            # Node right after left is LRU
            lru = self.left.next
            
            # Remove from list
            self.remove(lru)
            
            # Remove from hashmap using its key
            del self.cache[lru.key]