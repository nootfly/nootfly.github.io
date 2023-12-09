---
layout: post
title: "AI tools"
date: 2023-12-04 11:22:00 +1100
categories: tech
tags: algorithms
---

## problem

Given an array of numbers of length N, find both the minimum and maximum using less than 2 * (N - 2) comparisons.

## solution


```python
def find_min_max(arr):
    n = len(arr)
    
    # Initialize min and max
    if n % 2 == 0:
        if arr[0] > arr[1]:
            current_min, current_max = arr[1], arr[0]
        else:
            current_min, current_max = arr[0], arr[1]
        start = 2  # Start from the third element
    else:
        current_min = current_max = arr[0]
        start = 1  # Start from the second element

    # Iterate in pairs
    for i in range(start, n, 2):
        if arr[i] < arr[i + 1]:
            local_min, local_max = arr[i], arr[i + 1]
        else:
            local_min, local_max = arr[i + 1], arr[i]

        # Update global min and max
        if local_min < current_min:
            current_min = local_min
        if local_max > current_max:
            current_max = local_max

    return current_min, current_max

# Test the function
test_array = [3, 2, 5, 1, 8, 7, 4, 6]
find_min_max(test_array)
```

This function divides the array into pairs, compares the elements in each pair, and then updates the global minimum and maximum accordingly. It starts by checking if the array length is odd or even and initializes the minimum and maximum based on the first one or two elements. Then it iterates over the array in pairs, making comparisons. This method ensures a more efficient comparison count than a straightforward linear search.
