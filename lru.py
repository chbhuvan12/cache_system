import time
from node import Node

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.map = {}
        self.head = None
        self.tail = None

    def _remove(self, node):
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        if node == self.head:
            self.head = node.next
        if node == self.tail:
            self.tail = node.prev

    def _add_front(self, node):
        node.next = self.head
        if self.head:
            self.head.prev = node
        self.head = node
        if not self.tail:
            self.tail = node

    def get(self, key):
        if key not in self.map:
            return None
        node = self.map[key]
        self._remove(node)
        self._add_front(node)
        return node.value

    def put(self, key, value):
        if key in self.map:
            self._remove(self.map[key])
        elif len(self.map) == self.capacity:
            del self.map[self.tail.key]
            self._remove(self.tail)

        node = Node(key, value)
        self._add_front(node)
        self.map[key] = node
