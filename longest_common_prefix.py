'''
  Swear I thought they were asking for smt else - this code don't work so don't try it
  ["reflower","flow","flight"] how is the most common prefix to this nothing. I thought it was "fl"
'''


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs == []:
            return ""
        shortest = min(strs, key=len)
        longest_prefix = ""
        flag = True
        local_longest = ""

        for i in range(len(shortest)):
            local_longest += shortest[i]

            for word in strs:
                if local_longest not in word:
                    local_longest = local_longest[1:len(local_longest)]
                    break
            if len(local_longest) > len(longest_prefix):
                longest_prefix = local_longest

        return longest_prefix
