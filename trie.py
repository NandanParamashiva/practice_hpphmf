#!/usr/bin/python


class trie(): #nothing but a trie_node

    def __init__(self, terminate = False):
        self.data_map = {}
        self.is_leaf = terminate # if is_leaf is True:
                                 #  1. data_map should be empty
                                 #  2. And it represents that it's immediate parent node is the last character in the
                                 #     string through root.
                                 # Instead of having a special node(class) to indicate the leaf node,
                                 # we use the same trie_node and just mark is_leaf as True.

    def insert(self, str):
        self.insert_char(str, 0)

        return

    def remove(self, str):
        return

    def lookup(self, str):
        return

    def show(self, parent_string=""):
        if self.is_leaf:
            print parent_string
            return
        for ch in self.data_map:
            self.data_map[ch].show(parent_string + ch + ',')

    def insert_char(self, str, index):
        if (index >= len(str)):
            self.is_leaf = True
            return
        ch = str[index]
        if not self.data_map.has_key(ch) :
            self.data_map[ch] = trie()
        self.data_map[ch].insert_char(str, index+1)

def add_trie(pool, str):
    pool.insert(str)

def remove_trie(pool, str):
    pool.remove(str)

def lookup_trie(pool, str):
    pool.lookup(str)

def display_trie(pool):
    pool.show()

def main():
    str = 'testString'
    pool = trie()
    add_trie(pool, str)
    display_trie(pool)


if __name__ == '__main__':
    main()