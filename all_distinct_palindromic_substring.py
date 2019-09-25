'''
    An algorithm that'll return all distinct substring of a given string
'''
class Solution:
    def distinct_palindroms(self, s):
        if not s:
            return ''
        temp_sub = ''
        high = 0
        low = 0
        ret_list = []
        for count in range(len(s)-1):
            if s[count] == s[count+1]:
                high = count+1
                low = count
                while high < len(s) and low >= 0 and s[low] == s[high]:
                    temp_sub = s[low:high+1]
                    if temp_sub not in ret_list:
                        ret_list.append(temp_sub)
                    high += 1
                    low -= 1
                    
        for index in range(1, len(s)-1):
                high = index+1
                low = index-1
                while high < len(s) and low >= 0 and s[low] == s[high]:
                    temp_sub = s[low:high+1]
                    if temp_sub not in ret_list:
                        ret_list.append(temp_sub)
                    high += 1
                    low -= 1
        
        for element in list(s):
            ret_list.append(element)

        return ret_list
