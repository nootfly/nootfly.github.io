---
layout: post
title: "Algorithm - Max Circular Subarray"
date: 2023-12-10 9:30:00 +1100
categories: tech
tags: algorithms
---

## Problem
Given a circular array, compute its maximum subarray sum in O(n) time. A subarray can be empty, and in this case the sum is 0.

For example, given [8, -1, 3, 4], return 15 as we choose the numbers 3, 4, and 8 where the 8 is obtained from wrapping around.

Given [-4, 5, 1, 0], return 6 as we choose the numbers 5 and 1.

## Solution
To solve this problem, we can use Kadane's algorithm to find the maximum subarray sum for a linear array. However, since the array is circular, we need to consider two cases:

1. The maximum sum subarray does not wrap around the end of the array. This can be found using the standard Kadane's algorithm.
2. The maximum sum subarray wraps around the end of the array. To find this, we invert the sign of each element in the array and apply Kadane's algorithm to find the minimum subarray sum. The maximum sum in this case is the total sum of the array minus this minimum subarray sum.

We then return the maximum of these two sums. However, there's an edge case: if all numbers in the array are negative, the maximum sum is 0, as an empty subarray is allowed.

Let's write the Python function to implement this logic:

The Python function correctly solves the problem for the given examples:

1. For the array `[8, -1, 3, 4]`, the maximum subarray sum is `15`, achieved by choosing the numbers `3`, `4`, and `8` (where `8` is obtained from wrapping around).

2. For the array `[-4, 5, 1, 0]`, the maximum subarray sum is `6`, achieved by choosing the numbers `5` and `1`.

This solution runs in \( O(n) \) time, as required.


```python
def maxSubarraySumCircular(arr):
    def kadane(arr):
        max_ending_here = max_so_far = arr[0]
        for x in arr[1:]:
            max_ending_here = max(x, max_ending_here + x)
            max_so_far = max(max_so_far, max_ending_here)
        return max_so_far

    # Case 1: get the maximum sum using standard kadane's algorithm
    max_kadane = kadane(arr)

    # Case 2: Now find the maximum sum that includes corner elements.
    max_wrap = 0
    for i in range(len(arr)):
        max_wrap += arr[i]  # Calculate array-sum
        arr[i] = -arr[i]  # invert the array (change sign)

    # Max sum with corner elements will be:
    # array-sum - (-max subarray sum of inverted array)
    max_wrap = max_wrap + kadane(arr)

    # The maximum circular sum will be maximum of two sums
    if max_wrap > max_kadane and max_wrap != 0:
        return max_wrap
    else:
        return max_kadane

# Example usage:
example1 = [8, -1, 3, 4]
example2 = [-4, 5, 1, 0]

print(maxSubarraySumCircular(example1))  # Output: 15
print(maxSubarraySumCircular(example2))  # Output: 6
```

This code implements Kadane's algorithm for both the standard max subarray sum and the modified version for circular arrays. It handles the case where the maximum sum subarray either does not wrap around the array or does wrap around.