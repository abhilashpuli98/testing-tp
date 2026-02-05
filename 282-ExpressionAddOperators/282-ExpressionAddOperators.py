# Last Updated: 2/5/2026, 9:23:57 AM
class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        result=[]
        def backtrack(indx,curr_res,curr_sum,prevnum):
            if indx>=len(num):
                if curr_sum==target:
                    result.append("".join(curr_res))
                return
            else:
                for i in range(indx,len(num)):
                    curr_str=num[indx:i+1]
                    curr_num=int(curr_str)

                    if not curr_res:
                        backtrack(i+1,[curr_str],curr_num,curr_num)
                    else:
                        backtrack(i+1,curr_res+["+"]+[curr_str],curr_sum+curr_num,curr_num)
                        backtrack(i+1,curr_res+["-"]+[curr_str],curr_sum-curr_num,-curr_num)
                        backtrack(i+1,curr_res+["*"]+[curr_str],curr_sum-prevnum+curr_num*prevnum,curr_num*prevnum)
                    if num[indx]=='0':
                        break
        backtrack(0,[],0,0)
        return result
        