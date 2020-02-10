'''
    https://leetcode.com/explore/interview/card/microsoft/30/array-and-strings/213/
'''


class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        right = len(s) - 1
        left = 0
        # Swap the entire array
        while (right > left):
            temp = s[left]
            s[left] = s[right]
            s[right] = temp
            right -= 1
            left += 1

        right = left = count = 0
        while(count < len(s)):
            right = left = count
            # Getting the end of the current word
            while(right < len(s) and s[right] != ' '):
                right += 1
            count = right + 1
            right -= 1
            # Swap the characters and move inwards
            while(right > left):
                temp = s[left]
                s[left] = s[right]
                s[right] = temp
                right -= 1
                left += 1
