# Last Updated: 2/5/2026, 9:20:39 AM
class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        import re
        result=[]
        categories=["electronics","grocery","pharmacy","restaurant"]
        for i in range(len(code)):
            if bool(re.fullmatch(r"[a-zA-Z0-9_]+$",code[i])) and businessLine[i] in categories and isActive[i] :
                # We know how to deal with regex match 
                result.append([businessLine[i],code[i]])
        result.sort(key= lambda x : (x[0],x[1]))
        res=[]
        
        return [code for _,code in result]