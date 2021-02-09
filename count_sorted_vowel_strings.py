'''
  https://leetcode.com/problems/count-sorted-vowel-strings/
  honestly I wouldn't of thought of this solution... so rip again
'''


class Solution:
    def countVowelStrings(self, n: int) -> int:

        a = 5
        e = 4
        i = 3
        o = 2
        u = 1

        for k in range(0, n-1):
            u = u
            o = o+u
            i = i+o
            e = e+i
            a = a+e

        return a
