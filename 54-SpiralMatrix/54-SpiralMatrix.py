# Last Updated: 2/5/2026, 9:25:45 AM
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        cb,rb=0,0
        re,ce=len(matrix),len(matrix[0])
        result=[]
        n=len(matrix[0])
        total_eles=re*ce
        while len(result)<total_eles:
            for i in range(cb,ce):
                    result.append(matrix[rb][i])
            rb+=1
            for i in range(rb,re):
                    result.append(matrix[i][ce-1])
            ce-=1
            for i in range(ce-1,cb-1,-1):
                if rb<re:
                    result.append(matrix[re-1][i])
            re-=1 
            for i in range(re-1,rb-1,-1):
                if cb<ce:
                    result.append(matrix[i][cb])
            cb+=1
        return result

        