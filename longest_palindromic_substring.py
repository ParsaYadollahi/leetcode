'''
https://leetcode.com/problems/longest-palindromic-substring/
''''
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        s_list = list(s)
        if not s:
            return ''
        longest_sub = s[0]
        temp_sub = ''
        for count in range(len(s)-1):
            if s[count] == s[count+1]:
                high = count+1
                low = count
                while high < len(s) and low >= 0 and s[low] == s[high]:
                    temp_sub = s[low:high+1]
                    high += 1
                    low -= 1
                if len(temp_sub) > len(longest_sub):
                    longest_sub = temp_sub
                    
        for index in range(1, len(s)-1):
                low = index+1
                while high < len(s) and low >= 0 and s[low] == s[high]:
                    temp_sub = s[low:high+1]
                    high += 1
                    low -= 1
                if len(temp_sub) > len(longest_sub):
                    longest_sub = temp_sub
            
        return longest_sub
