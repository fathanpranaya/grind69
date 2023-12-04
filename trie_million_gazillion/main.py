class Trie(object):
    def __init__(self):
        self.root_node = {}

    def add_word(self, word):
        current_node = self.root_node
        is_new_word = False

        # work downwards through the trie, adding nodes
        # as needed, keeping track of whether we add any nodes.
        for char in word:
            if char not in current_node:
                is_new_word = True
                # assign current node char as current root
                current_node[char] = {}
            current_node = current_node[char]


        # explicitly mark the end of word.
        # Otherwise, we might say a word is present if it is a prefix of different,
        # longer word that was added earlier.
        if "EOW" not in current_node:
            is_new_word = True
            current_node["EOW"] = {}
            
        return is_new_word
    
    def print_content(self):
        print(f"{self.root_node}")

if __name__ == '__main__':
    print('trie')
    trie_urls =Trie()
    print(trie_urls.add_word("google.com"))
    print(trie_urls.add_word("google.com/maps"))
    print(trie_urls.add_word("gogle.com/maps"))
    print(trie_urls.add_word("gle.com/maps"))
    print(trie_urls.add_word("google.com/maps"))
    trie_urls.print_content()
