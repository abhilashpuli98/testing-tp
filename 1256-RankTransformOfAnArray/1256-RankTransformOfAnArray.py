# Last Updated: 2/5/2026, 9:22:32 AM
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        # it's BF solution TLE Arised
        """temp = sorted(list(set(arr))) #duplicates Matters here
        return [temp.index(val)+1 for val in arr  ]"""
        """    value_rank = {}
        unique_eles = sorted(list(set(arr)))
        for i in range(len(unique_eles)):
            value_rank[unique_eles[i]] = i+1
        for index in range(len(arr)):
            arr[index] = value_rank[arr[index]]
        return arr"""
        from scipy.stats import rankdata
        # Some Cool Stuff i Found Lol
        return [int(a) for a in rankdata(arr,method = 'dense')]