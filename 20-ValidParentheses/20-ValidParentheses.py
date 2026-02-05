# Last Updated: 2/5/2026, 9:26:13 AM
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack=[]
        for para in s:
            if para in '({[':
                stack.append(para)
            else:
                if not stack:
                    return False
                if para == ')' and stack[-1]!='(':
                    return False
                if para == ']' and stack[-1]!='[':
                    return False
                if para == '}' and stack[-1]!='{':
                    return False
                stack.pop()
        return not stack