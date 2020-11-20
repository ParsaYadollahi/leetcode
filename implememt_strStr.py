'''
  https://leetcode.com/problems/implement-strstr/
'''


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0

        if needle not in haystack:
            return -1

        for i in range(0, len(haystack) - len(needle)+1):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1
