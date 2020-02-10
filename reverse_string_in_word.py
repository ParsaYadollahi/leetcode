'''
    https://leetcode.com/problems/reverse-words-in-a-string-iii/
'''


class Solution:
    def reverseWords(self, s: str) -> str:
        s_arr = s.split()
        s = ''
        for count, word in enumerate(s_arr):
            s = (s+(word[::-1]) + ' ') if count != len(s_arr) - \
                1 else (s+(word[::-1]))
        return s
