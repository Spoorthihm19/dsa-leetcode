# Leetcode - 7

class Solution:
    def reverse(self, x: int) -> int:
        if x<0:
            y=int(str(abs(x))[::-1])
            y=-y
        else:
            y=int(str(x)[::-1])
        if y<-2**31 or y>2**31-1:
            return 0
        return y
