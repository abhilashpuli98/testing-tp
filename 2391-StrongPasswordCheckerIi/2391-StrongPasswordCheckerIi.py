# Last Updated: 3/13/2026, 10:09:01 AM
class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        if len(password)<8:
            return False
        lc=False
        uc=False
        digit=False
        spl=False
        anyadj=False
        for i in range(len(password)):
            if password[i].isalpha():
                if 'a'<=password[i]<='z':
                    lc=True
                elif 'A'<=password[i]<='Z':
                    uc=True
            if '0'<=password[i]<='9':
                digit=True
            if password[i] in "!@#$%^&*()-+":
                spl=True
            if i+1<len(password) and password[i] == password[i+1]:
                anyadj=True
        return True if lc and uc and digit and spl and not anyadj else False