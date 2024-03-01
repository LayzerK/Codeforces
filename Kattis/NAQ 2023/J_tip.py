import sys
input = sys.stdin.readline
def multiple_ints():
    return map(int, input().strip().split())


class Node():
    def __init__(self):
      self.children = {}
      self.words = 0
class And_Trie():
    def __init__(self):
        self.root = Node()
    
    def insert(self, word):
        
        curr = self.root
        n = len(word)

        for i, char in enumerate(word):
            opp = word[n-i-1]
            pair = (char, opp)
            if pair not in curr.children:
                curr.children[pair] = Node()
            curr.children[pair].words += 1
            curr = curr.children[pair]
    def count_matches(self, w1, w2):
        curr = self.root
        n = len(w1)
        for i, char in enumerate(w1):
            opp = w2[n-i-1]
            pair = (char, opp)
            if pair not in curr.children:
                return 0
            curr = curr.children[pair]
        return curr.words

class Trie():
    def __init__(self, isSuffix):
        self.root = Node()
        self.isSuffix = isSuffix
    
    def insert(self, word):
        
        curr = self.root


        for char in word:
            if char not in curr.children:
                curr.children[char] = Node()
            curr.children[char].words += 1
            curr = curr.children[char]
    def count_matches(self, word):
        
        curr = self.root

        for char in word:
            if char not in curr.children:
                return 0
            curr = curr.children[char]
        return curr.words


def solve():
    
    n,q = multiple_ints()

    and_trie = And_Trie()
    preTrie = Trie(False)
    suffTrie = Trie(True)
    


    for w in range(n):
        word = input().strip()
        
        preTrie.insert(word)
        suffTrie.insert(word[::-1])
        and_trie.insert(word)
    
    for query in range(q):
        
        q_type, w1, w2 = input().strip().split()
        
        and_val = and_trie.count_matches(w1, w2)
        preval = preTrie.count_matches(w1)
        suffval = suffTrie.count_matches(w2[::-1])

        or_val = preval + suffval - and_val

        xor_val = or_val - and_val

        #print("here", or_val, and_val, xor_val)
        #print(q_type, w1words, w2words)
        if q_type == "AND":
            print(and_val)
        elif q_type == "XOR":
            print(xor_val)
        else:
            print(or_val)
    
solve()
    