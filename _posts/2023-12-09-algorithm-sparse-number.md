---
layout: post
title: "Algorithm - find both the minimum and maximum"
date: 2023-12-09 17:50:00 +1100
categories: tech
tags: algorithms
---

## Problem
We say a number is sparse if there are no adjacent ones in its binary representation. For example, 21 (10101) is sparse, but 22 (10110) is not. For a given input N, find the smallest sparse number greater than or equal to N.

Do this in faster than O(N log N) time.

## Solution

Here is the Python code for finding the smallest sparse number greater than or equal to a given number \( N \):

```python
def next_sparse_number(n):
    # Convert the number to a binary string
    bin_n = list(bin(n)[2:])
    length = len(bin_n)
    max_set_bit = -1

    # Iterate over the binary string
    for i in range(1, length):
        if bin_n[i] == '1' and bin_n[i-1] == '1' and (max_set_bit < (i-1)):
            # Found two adjacent 1s, make changes to make the number sparse
            max_set_bit = i

            # Move to the left to find the bit which can be set
            while i >= 0 and bin_n[i] != '0':
                i -= 1

            # Set the found bit, make rest of the bits on right as 0
            if i >= 0:
                bin_n[i] = '1'
                for j in range(i+1, length):
                    bin_n[j] = '0'
            else:
                # If no such bit is found, add an extra bit at the top and set it
                bin_n = ['1'] + ['0' * length]

            # Convert the binary string back to an integer
            return int(''.join(bin_n), 2)

    # If the number is already sparse
    return n

# Example usage
n = 22
next_sparse_number(n)
```

This code efficiently finds the next sparse number for a given input \( N \) by manipulating its binary representation. For the example of \( N = 22 \), the function correctly returns \( 24 \) as the next sparse number.