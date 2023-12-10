---
layout: post
title: "Algorithm - Shortest unique prefix"
date: 2023-12-10 11:30:00 +1100
categories: tech
tags: algorithms
---

## Problem

Given a list of words, return the shortest unique prefix of each word. For example, given the list:
```
dog
cat
apple
apricot
fish
```
Return the list:
```
d
c
app
apr
f
```

## Solution
To solve this problem, we can use a trie, which is a tree-like data structure used for storing a dynamic set of strings where the keys are usually strings. Each node of the trie marks the end of a particular word and also contains links to nodes representing the next possible character in a word. Here's how we can use a trie for this problem:

1. **Build the Trie**: Insert each word from the list into the trie. While inserting, keep a count of how many words pass through each node.

2. **Find Shortest Unique Prefixes**: For each word, travel down the trie until you reach a node where the count is 1 (which means no other word shares that prefix) or the end of the word. The path to this node forms the shortest unique prefix for that word.

Certainly! Here's the Python code that finds the shortest unique prefix for each word in a given list:

```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.count += 1

    def shortest_unique_prefix(self, word):
        prefix = ''
        node = self.root
        for char in word:
            if node.count == 1:
                break
            prefix += char
            node = node.children[char]
        return prefix

def shortest_unique_prefixes(words):
    trie = Trie()
    for word in words:
        trie.insert(word)
    return [trie.shortest_unique_prefix(word) for word in words]

# Example usage:
words = ["dog", "cat", "apple", "apricot", "fish"]
print(shortest_unique_prefixes(words))  # Output: ['d', 'c', 'app', 'apr', 'f']
```

This code constructs a trie from the list of words, and then for each word, it finds the shortest prefix that is unique to that word within the trie.