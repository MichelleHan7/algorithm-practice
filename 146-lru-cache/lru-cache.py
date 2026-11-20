class Node:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dummy = Node()
        self.dummy.prev = self.dummy
        self.dummy.next = self.dummy
        self.key_to_node = {}

    def get(self, key: int) -> int:
        if key not in self.key_to_node:
            return -1
        node = self.key_to_node[key]
        self.remove(node)
        self.push_front(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.key_to_node:
            node = self.key_to_node[key]
            node.value = value
            self.remove(node)
            self.push_front(node)
        else:
            node = Node(key, value)
            self.key_to_node[key] = node
            self.push_front(node)
            if len(self.key_to_node) > self.capacity:
                back_node = self.dummy.prev
                del self.key_to_node[back_node.key]
                self.remove(back_node)
    
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