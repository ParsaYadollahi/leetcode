class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        sub_length = temp = 0
        arr = list(s)
        sub = ''
        
        for char in arr:
            
                sub = sub.split(char)[-1]
                sub = sub + char
                temp = len(sub)
                if temp > sub_length:
                    sub_length = temp            
                
        return sub_length
        
if __name__ == '__main__':
    # test cases
    sol = Solution()
    print(sol.lengthOfLongestSubstring('pwwkew'))
    print(sol.lengthOfLongestSubstring('bbbbb'))
    print(sol.lengthOfLongestSubstring('abcabcbb'))
    print(sol.lengthOfLongestSubstring(''))
    print(sol.lengthOfLongestSubstring('abdbdka'))

    