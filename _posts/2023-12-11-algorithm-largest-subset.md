---
layout: post
title: "Algorithm - Lrgest subset"
date: 2023-12-11 10:00:00 +1100
categories: tech
tags: algorithms
---

## Problem

Given a set of distinct positive integers, find the largest subset such that every pair of elements in the subset (i, j) satisfies either i % j = 0 or j % i = 0.

For example, given the set [3, 5, 10, 20, 21], you should return [5, 10, 20]. Given [1, 3, 6, 24], return [1, 3, 6, 24].


## Solution
To solve this problem, we can use a dynamic programming approach. The idea is to sort the array and then find the longest chain of numbers where every number is a multiple of its previous number in the chain. Here's a step-by-step solution:

1. **Sort the Array**: Sort the input array. Sorting is important because a multiple of a number will always be greater than or equal to the number.

2. **Dynamic Programming Array**: Create a DP array, where `dp[i]` represents the length of the longest subset ending with the `i`-th number in the sorted array. Also, maintain an array to store the previous index of the element in the longest subset chain.

3. **Initialize**: Initialize all elements of the DP array with 1, as every individual element is a subset in itself.

4. **Build the DP Array**: For each element at index `i`, check all previous elements `j` (0 to i-1). If the element at `i` is a multiple of the element at `j` and `dp[j] + 1 > dp[i]`, update `dp[i]` to `dp[j] + 1`, and update the previous index array.

5. **Find the Maximum**: Find the index with the maximum value in the DP array. This index corresponds to the last element of the largest subset.

6. **Reconstruct the Subset**: Starting from this index, use the previous index array to reconstruct the subset.

Here is the Python code implementing this approach:

```python
def largestDivisibleSubset(nums):
    if not nums:
        return []

    nums.sort()
    n = len(nums)
    dp = [1] * n
    prev = [-1] * n
    max_index = 0

    for i in range(1, n):
        for j in range(i):
            if nums[i] % nums[j] == 0 and dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
                prev[i] = j
        if dp[i] > dp[max_index]:
            max_index = i

    # Reconstruct the subset
    subset = []
    while max_index != -1:
        subset.append(nums[max_index])
        max_index = prev[max_index]

    return subset[::-1]  # reverse the subset

# Test the function
print(largestDivisibleSubset([3, 5, 10, 20, 21]))  # Output: [5, 10, 20]
print(largestDivisibleSubset([1, 3, 6, 24]))      # Output: [1, 3, 6, 24]
```

This code will output the largest subset where every pair satisfies the condition mentioned in the problem statement.
