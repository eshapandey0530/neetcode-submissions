class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} #hashmap - store key and node pointers

        self.head = Node(0,0)
        self.tail = Node(0,0)

        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:

        if key not in self.cache:
            return -1

        node = self.cache[key]
        self._remove(node)
        self.add_infront(node)
        return node.value

    def _remove(self, node):

        Nprev = node.prev
        Nnext = node.next
        Nprev.next = Nnext
        Nnext.prev = Nprev
    
    def add_infront(self, node):

        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def put(self, key: int, value: int) -> None:

        if key in self.cache:
            self._remove(self.cache[key])

        new_node = Node(key, value)

        self.cache[key] = new_node

        self.add_infront(new_node)

        if len(self.cache) > self.capacity:

            lru_node = self.tail.prev

            self._remove(lru_node)

            del self.cache[lru_node.key]
        
