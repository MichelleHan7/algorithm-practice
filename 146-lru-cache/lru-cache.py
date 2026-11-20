class Node:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dummy = Node()
        self.dummy.prev = self.dummy
        self.dummy.next = self.dummy
        self.key_to_node = {}

    def get(self, key: int) -> int:
        if key in self.key_to_node:
            node = self.key_to_node[key]
            self.remove(node)
            self.push_front(node)
            return node.value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key not in self.key_to_node:
            node = Node(key, value)
            self.key_to_node[key] = node
            self.push_front(node)
            if len(self.key_to_node) > self.capacity:
                last_node = self.dummy.prev
                del self.key_to_node[last_node.key]
                self.remove(last_node)
        else:
            self.key_to_node[key].value = value
            self.remove(self.key_to_node[key])
            self.push_front(self.key_to_node[key])

    
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def push_front(self, node):
        node.prev = self.dummy
        node.next = self.dummy.next
        self.dummy.next = node
        node.next.prev = node



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)