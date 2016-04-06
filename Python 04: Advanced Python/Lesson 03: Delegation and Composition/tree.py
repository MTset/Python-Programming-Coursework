"""
Created on Aug 18, 2011, modified Nov 05, 2015

@author: sholden
@modified by: m_tsikanovski
"""
class Tree:
    def __init__(self, key, value=None):
        "Create a new Tree object with empty L & R subtrees."
        self.key = key
        self.value = value
        self.left = self.right = None
        
    def insert(self, key, value=None):
        "Insert a new element into the tree in the correct position"
        if key < self.key:
            if self.left:
                self.left.insert(key, value)
            else:
                self.left = Tree(key, value)
        elif key > self.key:
            if self.right:
                self.right.insert(key, value)
            else:
                self.right = Tree(key, value)
        else:
            raise ValueError("Attempt to insert duplicate value")

    def find(self, key):
        "If key exist return node value associated with key, otherwise KeyError"
        if key not in self.walk():
            raise KeyError("Key '{0}' not found in Tree".format(key))
        elif key == self.key:
            return self.value
        elif key < self.key:
            if self.left:
                return self.left.find(key)
        elif key > self.key:
            if self.right:
                return self.right.find(key)
    
    def walk(self):
        "Generate the keys from the tree in sorted order."
        if self.left:
            for n in self.left.walk():
                yield n
        yield self.key
        if self.right:
            for  n in self.right.walk():
                yield n
                
if __name__ == "__main__":
    t = Tree("D", "Don")
    for c, d in [("B", "Bob"),("J", "Jack"), ("Q", "Quentin"), ("K", "Karen"),
                  ("F", "Fred"), ("A", "Andrew"), ("C", "Cathy")]:
        t.insert(c, d)

    print(list(t.walk()))
    print(t.find("J"))