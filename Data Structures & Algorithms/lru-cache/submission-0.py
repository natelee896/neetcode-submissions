class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.head = Node(None, None)
        self.tail = Node(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head.next
    
    def addNode(self, node):
        node.next = self.head.next
        node.prev = self.head

        self.head.next.prev = node 
        self.head.next = node
    
    def removeNode(self, node):
        p, n = node.prev, node.next

        p.next = n
        n.prev = p
    
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        node = self.cache[key]
        self.removeNode(node)
        self.addNode(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            self.removeNode(node)

        node = Node(key, value)
        self.cache[key] = node
        self.addNode(node)

        if len(self.cache) > self.capacity:
            lru = self.tail.prev
            self.removeNode(lru)
            del self.cache[lru.key]
        
