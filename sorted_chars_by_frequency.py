'''
    https://leetcode.com/problems/sort-characters-by-frequency/
'''


class Solution:
    def frequencySort(self, s: str) -> str:
        d = {}
        for char in s:
            if char in d:
                d[char] += 1
            else:
                d.setdefault(char, 1)

        d = {k: v for k, v in sorted(
            d.items(), key=lambda char: char[1], reverse=True)}
        ret_string = ''
        for item in d.items():
            ret_string += (item[1]*item[0])

        return ret_string
