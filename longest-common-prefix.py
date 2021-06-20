'''
    https://leetcode.com/problems/longest-common-prefix
'''
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest_prefix = strs[0]

        for i in range(len(strs)):
            longest_prefix = self.longestPrefix(longest_prefix, strs[i])

        return longest_prefix


    def longestPrefix(self, str1, str2):
        longest_prefix = ''
        i = 0
        while(i < len(str1) and i < len(str2)):

            if str1[i] in str2[i]:
                longest_prefix = str1[0:i+1]
            else:
                return longest_prefix
            i += 1

        return longest_prefix
