# dsa-week-01-day-008

# LeetCode 7 – Reverse Integer

## Problem
Reverse the digits of a signed integer. Return `0` if the reversed number exceeds the 32-bit signed integer range.

## Python Solution

```python
class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            y = int(str(abs(x))[::-1])
            y = -y
        else:
            y = int(str(x)[::-1])

        if y < -2**31 or y > 2**31 - 1:
            return 0

        return y
```

## Approach
- Handle negative numbers using `abs()`.
- Reverse digits using string slicing `[::-1]`.
- Convert the result back to an integer.
- Check the 32-bit integer limit.

## Complexity
- **Time:** O(log n)
- **Space:** O(log n)

## Concepts
String Slicing, Type Conversion, Conditional Statements.

**LeetCode:** [7. Reverse Integer](https://leetcode.com/problems/reverse-integer/)

**Language:** Python 3 | **Difficulty:** Medium
