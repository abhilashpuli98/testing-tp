# Last Updated: 3/13/2026, 10:09:14 AM
from collections import deque

class Solution:
    def validPath(self, n, edges, source, destination):
        g = {}
        for a, b in edges:
            if a not in g:
                g[a] = []
            if b not in g:
                g[b] = []
            g[a].append(b)
            g[b].append(a)
        q = deque([source])
        visit = set()
        visit.add(source)
        while q:
            x = q.popleft()
            if x == destination:
                return True
            for i in g[x]:
                if i not in visit:
                    visit.add(i)
                    q.append(i)
        return False