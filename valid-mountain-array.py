'''
  https://leetcode.com/problems/valid-mountain-array
  this one question made me question why im in SWE....
'''


class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False

        increase = arr[1] > arr[0]
        if not increase:
            return False

        for i in range(1, len(arr)):

            if increase == True and arr[i-1] >= arr[i]:  # switch to down
                increase = False

            if increase == True and arr[i-1] >= arr[i]:  # going up
                return False
            elif increase == False and arr[i-1] <= arr[i]:  # going down
                return False

        return True if not increase else False
