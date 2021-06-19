'''
    https://leetcode.com/problems/duplicate-zeros/
'''
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        num_zeros = 0
        length = len(arr) - 1
        for i in range(len(arr)):
            if i > length - num_zeros:
                break
            if arr[i] == 0:
                if i == length - num_zeros:
                    arr[length] = 0
                    length -= 1
                    break
                num_zeros += 1


        p1, p2 = length - num_zeros, length


        for i in range(p1, -1, -1):
            if arr[p1] == 0:
                arr[p2] = 0
                p2 -= 1
                arr[p2] = 0
                p1 -= 1
                p2 -= 1
            else:
                arr[p2] = arr[p1]
                p1 -= 1
                p2 -= 1
