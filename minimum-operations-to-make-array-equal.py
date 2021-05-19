'''
    minimum-operations-to-make-array-equal
'''
class Solution:
    def minOperations(self, n: int) -> int:
        count = 0
        diff = ((2*(n-1)+1) - (2*((n-1)//2 + (n-1)%2) + 1))
        while(diff >= 0 ):
            count += diff
            diff -= 2

        if (n%2 == 0):
            count += n//2
        return count
