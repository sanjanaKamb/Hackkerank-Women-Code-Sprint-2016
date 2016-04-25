from collections import namedtuple, deque

inf = float('inf')
Edge = namedtuple('Edge', 'start, end, cost')
class outer(object):
    class Graph():
        def __init__(self, edges):
            self.edges = edges2 = [Edge(*edge) for edge in edges]
            self.vertices = set(sum(([e.start, e.end] for e in edges2), []))

        def dijkstra(self, source, dest):
            assert source in self.vertices
            dist = {vertex: inf for vertex in self.vertices}
            previous = {vertex: None for vertex in self.vertices}
            dist[source] = 0
            q = self.vertices.copy()
            neighbours = {vertex: set() for vertex in self.vertices}
            for start, end, cost in self.edges:
                neighbours[start].add((end, cost))


            while q:
                u = min(q, key=lambda vertex: dist[vertex])
                q.remove(u)
                if dist[u] == inf or u == dest:
                    break
                for v, cost in neighbours[u]:
                    alt = dist[u] + cost
                    if alt < dist[v]:                                  # Relax (u,v,a)
                        dist[v] = alt
                        previous[v] = u

            s, u = deque(), dest
            while previous[u]:
                s.appendleft(u)
                u = previous[u]
            s.appendleft(u)
            return s
    def containsAll(list):
        for i in list:
            if i[2]!=50000:
                return False
        return True
        
    T = int(raw_input().strip())
    for some in range(0,T):
        a = raw_input().strip().split(' ')
        b = raw_input().strip().split(' ')
        N = int(a[0])
        M = int(a[1])
        S = b[0]
        D = b[1]
        edgeL=[]
        for some2 in range(0,M):
            c = raw_input().strip().split(' ')
            edgeL.append((c[0],c[1],int(c[2])))
        smallest = 0
        second =0
        third =0
        notFound = False;
        while True:
            if third>0:
                break
            if containsAll(edgeL):
                notFound = True
                break
            graph = Graph(edgeL)
            l = list(graph.dijkstra(S, D))
            sum = 0
            for i in range(0,len(l)):
                if i == len(l)-1:
                    break
                for j in range(0,len(edgeL)):

                    if l[i]==edgeL[j][0] and l[i+1]==edgeL[j][1]:
                        sum = sum+ edgeL[j][2]
                        edgeL[j] = (edgeL[j][0],edgeL[j][1],50001)
                        break
            if smallest == 0:
                smallest = sum
            elif sum>smallest and second ==0:
                second = sum
            elif sum>smallest and sum>second and third ==0:
                third = sum
        if third != 0:
            print third
        else:
            print -1