'''
https://leetcode.com/problems/container-with-most-water/
'''
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_container = 0
        temp_container = 0
        for index, value in enumerate(height):
            i = 0
            while i < index:
                y = height[i]
                dist = index-i
                if y < value:
                    h_diff = y
                else:
                    h_diff = value

                temp_container = h_diff * dist
                i += 1

                if max_container < temp_container:
                    max_container = temp_container

        return max_container



class Solution2(object):
    def maxArea2(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_container = 0
        temp_container = 0
        left = 0
        right = len(height)-1

        while left != right:

            if height[right] < height[left]:
                y_diff = height[right]
            else:
                y_diff = height[left]
            temp_container = (right - left) * y_diff

            if max_container < temp_container:
                max_container = temp_container

            if height[right] > height[left]:
                left += 1
            else:
                right -= 1
        return max_container

class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_container = 0
        temp_container = 0
        left, right = 0, len(height) - 1

        while(left < right):
            temp_container = min(height[left], height[right]) * (right - left)

            if temp_container > max_container:
                max_container = temp_container

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_container
