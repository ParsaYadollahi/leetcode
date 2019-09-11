'''
https://leetcode.com/problems/zigzag-conversion/
'''
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        
        rows = [[] for i in range(numRows)]

        increment_flag = True
        index = 0
        for c in s:
            rows[index] += c
            if index == numRows-1:
                increment_flag = False
            elif index == 0:
                increment_flag = True
            if increment_flag:
                index += 1
            else:
                index -= 1

        rows = ''.join(''.join(i) for i in rows)
        return rows