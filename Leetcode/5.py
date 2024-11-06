import math
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 1: return s
        s1=""
        for i in range(2):
            for j in range(len(s)-1):
                if s[j:] == s[j:][::-1]:
                    return s[j:]
            s=s[::-1]
        for i in range(math.ceil(len(s)/2)):
            # print(math.ceil(len(s[j:])/2))
            s1=s[i:len(s)-i]
            s2=s1[::-1]
            if s2==s1:
                return s1
            s1=""
        if s1=="": return s[0]
s=Solution()
print(s.longestPalindrome("aacabdkacaa"))