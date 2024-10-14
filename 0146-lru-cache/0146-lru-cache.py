class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None 

class LRUCache:

    def __init__(self, capacity: int):
        # left = least recently used
        # right = most recently used
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next = self.right 
        self.right.prev = self.left 
        
        self.cache = {}
        self.capacity = capacity
        
        
    # remove node from list
    def remove(self, node):
        prev = node.prev
        nxt = node.next
        prev.next, nxt.prev = nxt, prev
        
        
    # insert node at right
    def insert(self, node):
        prev = self.right.prev
        nxt = self.right
        node.prev, prev.next = prev, node
        node.next, nxt.prev = nxt, node
        

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            return node.val
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        
        new_node = Node(key, value)    
        self.insert(new_node)
        self.cache[key] = new_node
            
        # check if we've exceeded capacity
        if len(self.cache) > self.capacity:
            lru_node = self.left.next
            self.remove(lru_node)
            del self.cache[lru_node.key]
            
        
      
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)