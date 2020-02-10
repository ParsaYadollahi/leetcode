'''
    https://leetcode.com/explore/interview/card/microsoft/30/array-and-strings/166/
'''


class Solution:
    def remove_spaces(self, s):

        count = 0
        c = s[0]
        while c == ' ' and count < len(s):
            count += 1
            c = s[count]
        s = s[count:]

        count = len(s)-1
        c = s[count]
        while c == ' ' and count > len(s):
            count -= 1
            c = s[:count]
        return s

    def reverseWords(self, s: str) -> str:
        if s.split() == [] or s == '':
            return ''
        s = self.remove_spaces(s)
        s = s[::-1]
        s = s.split()
        print(s)
        ret_string = ''
        for word in range(len(s)):
            ret_string += ((s[word][::-1] + ' ') if word <
                           len(s)-1 else s[word][::-1])
        return ret_string
