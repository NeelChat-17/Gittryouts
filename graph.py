# Building from scratch
class GraphProblem:

    def graphing(self, edges, N, src):

        graph = {}

        for u,v in edges:
            if u not in graph:
                graph[u] = [v]
            elif u in graph:
                graph[u].append(v)
            
            if v not in graph:
                graph[v] = [u]
            elif v in graph:
                graph[v].append(u)

        dist = [float('inf')] * N
        dist[src] = 0

        q = []
        q.append(src)

        while q:
            node = q.pop()
            for i in graph[node]:
                if dist[node]+1 < dist[i]:
                    dist[i] = dist[node]+1
                    q.append(i)

        for i in range(N):
            if dist[i] == float('inf'):
                dist[i] = -1
            
        return dist
        
    
if __name__ == "__main__":
    gp = GraphProblem()
    edges = [[1,0],[2,1],[0,3],[3,7],[3,4],[7,4],[7,6],[4,5],[4,6],[6,5]]
    N = 8
    M = 10
    src = 0 
    result = gp.graphing(edges, N, src)
    print(" ".join(map(str,result)))


        