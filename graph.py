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

        print(graph)
        print(dist)
        print(q)
        
    
if __name__ == "__main__":
    gp = GraphProblem()
    edges = [[1,0],[2,1],[0,3],[3,7],[3,4],[7,4],[7,6],[4,5],[4,6],[6,5]] 
    gp.graphing(edges, 3, 0)

        