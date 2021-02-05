'''
  https://leetcode.com/problems/longest-substring-without-repeating-characters/
  Rip the first one I did was cleaner
'''


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = ''
        substring = ''
        left, right = 0, 0

        while(right < len(s)):
            if s[right] not in substring:
                substring += (s[right])
                right += 1
            else:
                while (s[left] != s[right]):
                    left += 1
                left += 1
                substring = s[left:right]

            if len(substring) > len(longest):
                longest = substring

        return len(longest)
