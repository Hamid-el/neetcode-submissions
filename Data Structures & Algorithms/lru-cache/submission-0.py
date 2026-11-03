class Node:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # key -> Node
        self.head = Node(0, 0) #  lru immer letztes element in linkedlist
        self.tail = Node(0, 0)

        self.head.next = self.tail
        self.tail.prev = self.head
    
    def remove(self, node):
        # [1] ⇄ [2] ⇄ [3] ⇄ [4]
        n = node
        n.prev.next = n.next
        n.next.prev = n.prev

    def insert(self, node): # inserts after head
        # HEAD ⇄ [1] ⇄ [2] ⇄ [3] ⇄ [4]
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        node = self.cache[key]
        self.remove(node)
        self.insert(node)
        return node.value
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node) # remove and add later because lru
            node.value = value
            self.insert(node)
        else:
            node = Node(key, value)
            self.cache[key] = node
            self.insert(node)

        if len(self.cache) > self.capacity:
            lru = self.tail.prev
            self.remove(lru)
            del self.cache[lru.key] # or self.cache.pop(lru.key)
        

        
