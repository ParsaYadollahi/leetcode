'''
    https://leetcode.com/problems/first-unique-character-in-a-string
'''
class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {}
        for i in range(len(s)):
            if s[i] not in d:
                d[s[i]] = i
            else:
                d[s[i]] = -1

        for c in d:
            if d[c] != -1:
                return d[c]

        return -1


    def firstUniqChar(self, s: str) -> int:
        d = {}
        for i in range(len(s)):
            if s[i] not in d:
                d[s[i]] = 1
            else:
                d[s[i]] += 1

        for i in range(len(s)):
            if d[s[i]] == 1:
                return i

        return -1
