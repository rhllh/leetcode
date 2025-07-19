"""
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. 
Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, 
evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.

Input:
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output:
[null, null, null, 1, null, -1, null, -1, 3, 4]

Constraints:
1 <= capacity <= 3000
0 <= key <= 104
0 <= value <= 105
At most 2 * 105 calls will be made to get and put.
"""
class Node:
    def __init__(self, key: int, val: int):
        self.key, self.val = key, val
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.cache:
            # move key node to front of list
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # remove
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])
        
        # check capacity
        if len(self.cache) > self.cap:
            lru = self.tail.prev
            self.remove(lru)
            del self.cache[lru.key]
        
    def remove(self, node: Node):
        # remove from the end
        nxt = node.next
        prv = node.prev
        
        prv.next = nxt
        nxt.prev = prv
        
    def insert(self, node: Node):
        # insert at front
        prv = self.head
        nxt = self.head.next
        
        prv.next = node
        node.prev = prv
        
        nxt.prev = node
        node.next = nxt