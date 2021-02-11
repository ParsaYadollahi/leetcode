'''
  https://leetcode.com/problems/determine-if-two-strings-are-close/
  spent 30 mins trying it to find out i read it wrong...
'''


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:

        if len(word1) != len(word2):
            return False

#         d1, d2 = {}, {}

#         for c in word1:
#             if c not in d1:
#                 d1.setdefault(c, 1)
#             else:
#                 d1[c] += 1

#         for c in word2:
#             if c not in d2:
#                 d2.setdefault(c, 1)
#             else:
#                 d2[c] += 1


#         for c in d1.keys():
#             if c not in d2:
#                 return False

#         l1 = sorted(d1.values())
#         l2 = sorted(d2.values())

#         if l1 != l2:
#             return False

#         return True

        l1 = [0 for i in range(26)]
        l2 = [0 for i in range(26)]

        for i in range(len(word1)):
            l1[ord(word1[i]) - ord('a')] += 1
            l2[ord(word2[i]) - ord('a')] += 1

        for i in range(26):
            if ((l1[i] == 0 and l2[i] != 0) or (l1[i] != 0 and l2[i] == 0)):
                return False

        if sorted(l1) != sorted(l2):
            return False

        return True
