# Last Updated: 2/5/2026, 9:40:35 PM
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        lett_dict={
            '2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'
        }
        letters=[]
        for digit in digits:
            letters.append(list(lett_dict[digit]))
        while len(letters)>1:
            let1=letters.pop()
            let2=letters.pop()
            comb=[]
            for i in let1:
                for j in let2:
                    comb.append(j+i)
            letters.append(comb)
        return letters[0] if letters else []