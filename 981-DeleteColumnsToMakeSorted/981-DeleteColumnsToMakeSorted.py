# Last Updated: 2/5/2026, 9:22:46 AM
class Solution(object):
    def minDeletionSize(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        count=0
        for i in range(len(strs[0])):
            letters=[]
            for j in range(len(strs)):
                letters.append(strs[j][i])
            if letters != sorted(letters):
                count+=1
        return count
        