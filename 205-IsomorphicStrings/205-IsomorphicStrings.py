# Last Updated: 2/5/2026, 9:24:18 AM
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        """Works well
        if len(s)!=len(t):
            return False
        map_st={}
        map_ts={}
        for schar,tchar in zip(s,t):
            if (schar in map_st and map_st[schar]!=tchar )or (tchar in map_ts and map_ts[tchar]!=schar):
                return False
            map_st[schar]=tchar
            map_ts[tchar]=schar
        return True"""
        return len(set(zip(s,t))) == len(set(s)) ==len(set(t))
                 
            
        