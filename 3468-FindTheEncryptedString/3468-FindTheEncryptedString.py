# Last Updated: 2/5/2026, 9:21:21 AM
class Solution(object):
    def getEncryptedString(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
 
        n = len(s)
        k = k % n  # effective shift to handle large k values
        encrypted_string = []
    
        for i in range(n):
            new_index = (i + k) % n
            encrypted_string.append(s[new_index])
    
        return ''.join(encrypted_string)


                