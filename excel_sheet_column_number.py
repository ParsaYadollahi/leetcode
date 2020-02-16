'''
    https://leetcode.com/explore/interview/card/microsoft/48/others/183/
'''


class Solution:
    def func(self, i, char_index):
        return (26**i*char_index)

    def titleToNumber(self, s: str) -> int:
        map = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
               'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

        if len(s) == 0:
            return 0
        if len(s) == 1:
            return map.index(s[0])+1

        s = s[::-1]
        total = 0
        for i in range(len(s)):
            total += self.func(i, map.index(s[i])+1)

        return total
