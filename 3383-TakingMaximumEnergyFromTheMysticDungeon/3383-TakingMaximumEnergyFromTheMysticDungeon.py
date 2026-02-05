# Last Updated: 2/5/2026, 9:21:38 AM
class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        maxEnergy = float('-inf')
        energySequence = [0]*len(energy)
        for x in range(len(energy)-1,-1,-1):
            energySequence[x] = energy[x]+(energySequence[x+k] if x+k<len(energy) else 0)
            maxEnergy = max(maxEnergy,energySequence[x])
        return maxEnergy
