from util import Stack, Queue
# Given two words (begin_word and end_word)
# and a dictionary's word list, return the shortest transformation
# sequence from begin_word to end_word, such that: 

# Only one letter can be changed at a time.
# Each transformed word must exist in the word list.
# Note that begin_word is not a transformed word.
# Note:

# Return None if there is no such transformation sequence.
# All words contain only lowercase alphabetic characters.
# you may assume not duplicates in the word list.
# you may assume 
#2 build the graph
#load words from dictionary
f = open.('words.txt', 'r')
words = f.read().lower().split("\n")

def get_neighbors(word):
    result = []
    pass

def words_are_neighbors(w1, w2):
    """return True if words are one letter apart
    false otherwise"""
    list_word = list(w1)
    for i in range (len(list_word)):
        for letter in ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        temp_word = list_word.copy()
        temp_word[i] = letter
        if "".join(temp_word) == w2:
            return True
    return False
#3 traverse the graph(BFS)
def word_ladder(self, begin_word, end_word):
    # create a queue
    q = Queue
    # enqueue a path to starting word 
    q.enqueue( [begin_word] )
    # create a visited set 
    # while queue is not empty:
        # dequeue path
        # Grab the las word from the path
        # Check if it's our target word
        # Check if it's been visited
        # if not, mark as visited
            # enqueue path to each neighboring word

