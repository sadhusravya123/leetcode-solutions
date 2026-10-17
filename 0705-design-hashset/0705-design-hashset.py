class MyHashSet(object):

    def __init__(self):
        self.s = []

    def add(self, key):
        if key not in self.s:
            self.s.append(key)

    def remove(self, key):
        if key in self.s:
            self.s.remove(key)

    def contains(self, key):
        return key in self.s