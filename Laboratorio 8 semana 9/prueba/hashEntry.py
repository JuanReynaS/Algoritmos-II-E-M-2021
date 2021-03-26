class HashEntry(object):
    """docstring for Dlist"""

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None
