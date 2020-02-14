'''
    https://leetcode.com/explore/interview/card/microsoft/47/sorting-and-searching/191/
'''


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Return the pivot index
        def find_pivot(nums):
            if nums[0] < nums[-1]:  # means in increasing order
                return 0
            # indices
            l = 0
            r = len(nums)-1
            mid = r//2
            # loop until the left meets the right index
            while(l <= r):
                # if the number that comes after the pivot is bigger ==> found pivot
                if nums[mid] > nums[mid+1]:
                    return mid+1

                else:
                    # the mid is greater than the left point ==> pivot
                    if nums[l] > nums[mid]:
                        r = mid - 1
                    else:  # the pivot is on the right side
                        l = mid + 1
                # Re-Calculate mid
                mid = (l + r)//2

        def binary_search(l, r):
            # Binary Search left and right
            while(l <= r):
                # Refresh mid point
                mid = (l + r)//2
                # found the elemnent
                if nums[mid] == target:
                    return mid
                else:
                    # if the middle element is smaller than right target ==> on the right side
                    if target > nums[mid]:
                        l = mid + 1
                    else:
                        # ELement is somewhere on the right
                        r = mid - 1
            return -1

        # basic checks
        if len(nums) == 0:
            return -1
        if len(nums) == 1:
            return 0 if nums[0] == target else -1

        # find the pivot where the array turned
        pivot = find_pivot(nums)
        # pivot = target
        print(pivot)
        if nums[pivot] == target:
            return pivot

        # binary search the entire array
        if pivot == 0:
            return binary_search(0, len(nums)-1)
        # Target is smaller than the last element. Search the begining of the list
        if target > nums[-1]:
            return binary_search(0, pivot)
        else:
            # Target is greater than the last element. Search the end of the list
            return binary_search(pivot, len(nums)-1)
