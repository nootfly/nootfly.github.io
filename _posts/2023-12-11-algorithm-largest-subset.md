---
layout: post
title: "Algorithm - Largest subset"
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


Let's break down the code and its components for clarity:

### Sorting the Array

```python
nums.sort()
```
The array is sorted because we need to ensure that for any pair of elements `i, j` in the subset, where `i` is a multiple of `j`, `i` must come after `j` in the sorted order. Sorting makes it easier to find such pairs sequentially.

### Dynamic Programming Array: `dp`

```python
dp = [1] * n
```
The `dp` array is used for dynamic programming. `dp[i]` stores the length of the longest subset of the array ending with the `i`-th element in the sorted array where each pair of elements satisfies the given condition. Initially, all elements are initialized to 1, since each number individually forms a valid subset.

### Previous Index Array: `prev`

```python
prev = [-1] * n
```
The `prev` array is crucial for reconstructing the subset at the end. `prev[i]` stores the index of the previous element in the subset ending with the `i`-th element. We initialize `prev` with `-1` to indicate that there is no previous element in the subset for any element initially.

### Building the DP Array

```python
for i in range(1, n):
    for j in range(i):
        if nums[i] % nums[j] == 0 and dp[j] + 1 > dp[i]:
            dp[i] = dp[j] + 1
            prev[i] = j
```
Here, for each element at index `i`, we check all elements `j` before it. If `nums[i]` is a multiple of `nums[j]` and adding `nums[i]` to the subset ending at `nums[j]` increases the subset size, we update `dp[i]` and set `prev[i]` to `j`. This step effectively builds the longest subset chain ending at each index `i`.

### Finding the Maximum Subset Length and Index

```python
max_index = 0
for i in range(1, n):
    if dp[i] > dp[max_index]:
        max_index = i
```
After filling the `dp` array, we find the index `max_index` where the maximum subset length is stored. This index corresponds to the end of the longest divisible subset.

### Reconstructing the Subset

```python
subset = []
while max_index != -1:
    subset.append(nums[max_index])
    max_index = prev[max_index]
```
Starting from `max_index`, we use the `prev` array to trace back through the indices of the elements in the subset. We keep adding the corresponding elements to the `subset` list and move to the previous index as indicated by `prev`. We stop when `max_index` becomes `-1`, indicating the start of the subset.

### Example

Let's consider an example with the array `[1, 2, 3]`:

1. **Sort**: `[1, 2, 3]`
2. **DP Initialization**: `dp = [1, 1, 1]`, `prev = [-1, -1, -1]`
3. **Building DP**:
   - For `i = 1 (num = 2)`, `j = 0 (num = 1)`, `2 % 1 == 0`, update `dp[1]` to `2`, `prev[1]` to `0`.
   - For `i = 2 (num = 3)`, no `j` satisfies the condition.
4. **Maximum Index**: `max_index = 1`
5. **Reconstruct Subset**: Start from `max_index = 1`, subset = `[2]`, previous index = `0`, subset = `[1, 2]`.

This approach ensures we find the largest subset where each pair of elements satisfies the condition either `i % j == 0` or `j % i == 0`.
