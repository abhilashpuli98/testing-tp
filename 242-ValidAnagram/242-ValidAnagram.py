# Last Updated: 2/5/2026, 9:24:01 AM
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_count=[0]*26
        t_count=[0]*26
        for i in range(len(s)):
            s_count[ord(s[i])-ord('a')]+=1
        for i in range(len(t)):
            indx=ord(t[i])-ord('a')
            t_count[indx]+=1
            if t_count[indx]>s_count[indx]:
                return False
        for i in range(26):
            if t_count[i]!=s_count[i]:
                return False
        return True
        