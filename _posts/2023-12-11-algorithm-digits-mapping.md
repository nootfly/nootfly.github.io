---
layout: post
title: "Algorithm - Mapping of digits to letters"
date: 2023-12-11 23:00:00 +1100
categories: tech
tags: algorithms
---

## Problem

Given a mapping of digits to letters (as in a phone number), and a digit string, return all possible letters the number could represent. You can assume each valid number in the mapping is a single digit.

For example if {“2”: [“a”, “b”, “c”], 3: [“d”, “e”, “f”], …} then “23” should return [“ad”, “ae”, “af”, “bd”, “be”, “bf”, “cd”, “ce”, “cf"].


## Solution
To solve this problem, we can use a technique called backtracking, which is a form of recursion. The idea is to iterate through each digit in the input string, find the corresponding letters for that digit, and then recursively build combinations of letters for the remaining digits.

Here's the step-by-step approach and the corresponding Python code:

1. **Map Digits to Letters**: First, we define a mapping from digits to their corresponding letters.

2. **Backtracking Function**: We use a helper function that takes the current combination of letters and the next index of the digit to process.

3. **Recursive Calls**: For each letter corresponding to the current digit, we add the letter to the current combination and call the function recursively for the next digit.

4. **Base Case**: When the length of the combination equals the length of the digit string, we add the combination to the result.

5. **Initiate Backtracking**: Start the process with an empty string and index 0.

Here's the Python implementation:

```python
def letterCombinations(digits):
    if not digits:
        return []

    digit_to_char = {
        "2": ["a", "b", "c"],
        "3": ["d", "e", "f"],
        "4": ["g", "h", "i"],
        "5": ["j", "k", "l"],
        "6": ["m", "n", "o"],
        "7": ["p", "q", "r", "s"],
        "8": ["t", "u", "v"],
        "9": ["w", "x", "y", "z"]
    }

    def backtrack(index, path):
        # If the path is the same length as digits, we have a complete combination
        if len(path) == len(digits):
            combinations.append("".join(path))
            return
        
        # Get the letters that the current digit maps to, and loop through them
        possible_letters = digit_to_char[digits[index]]
        for letter in possible_letters:
            # Add the letter to our current path
            path.append(letter)
            # Move on to the next digit
            backtrack(index + 1, path)
            # Backtrack by removing the letter before moving onto the next
            path.pop()

    combinations = []
    backtrack(0, [])
    return combinations

# Test the function
print(letterCombinations("23"))
```

This code will generate all possible letter combinations for the given digit string using the specified digit-to-letter mapping.