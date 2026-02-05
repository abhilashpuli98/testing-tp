# Last Updated: 2/5/2026, 9:23:26 AM
class Solution:
    def originalDigits(self, s: str) -> str:
        counter=[0]*26
        for letter in s:
            counter[ord(letter)-ord('a')]+=1
        digit=[0]*10
        digit[0]=counter[ord('z')-ord('a')]
        digit[2]=counter[ord('w')-ord('a')]
        digit[4]=counter[ord('u')-ord('a')]
        digit[6]=counter[ord('x')-ord('a')]
        digit[8]=counter[ord('g')-ord('a')]
        digit[1]=counter[ord('o')-ord('a')]-digit[0]-digit[2]-digit[4]
        digit[3]=counter[ord('r')-ord('a')]-digit[4]-digit[0]
        digit[5]=counter[ord('f')-ord('a')]-digit[4]
        digit[7]=counter[ord('s')-ord('a')]-digit[6]
        digit[9]=(counter[ord('n')-ord('a')]-digit[1]-digit[7])//2
        #digit[9]=(counter[ord('i')-ord('a')]-digit[5]-digit[6]-digit[8])
        return "".join(str(i)*digit[i] for i in range(10))
                    
                    