'''
    https://leetcode.com/problems/find-all-anagrams-in-a-string/
'''
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        pdict = [0] * 27
        sdict = [0] * 27

        for i in range(len(p)):
            pdict[ord(p[i]) - ord('a')] += 1

        window = len(p)
        res = []
        length = len(s) - window

        j = 0
        for i in range(len(s)):
            while(j < len(s) and j - i < window):
                sdict[ord(s[j]) - ord('a')] += 1
                j += 1

            if sdict == pdict:
                res.append(i)
            sdict[ord(s[i]) - ord('a')] -= 1
        return res
