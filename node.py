class Node:
    def __init__(self, key, value, expiry=None):
        self.key = key
        self.value = value
        self.expiry = expiry
        self.prev = None
        self.next = None
