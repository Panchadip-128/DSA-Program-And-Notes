# time- O(N*E) as each edge will get relaxed 'n' times, E= no of edges, N= no of vertices
def BellmanFord(src,edges,n):
    distance= [999999]*n
    distance[src]= 0
    # to get the optimal ans if there is no negative weight cycle
    for i in range(n-1):
        tempDistance= distance.copy()
        for s,d,w in edges:
            if distance[s]==999999:
                continue
            if tempDistance[d]> distance[s] +w:
                tempDistance[d]= distance[s] + w
        distance= tempDistance.copy()
    
    # now to check the negative cycle
    for s,d,w in edges:
        if distance[s]!= 999999 and distance[d] > distance[s] + w:
            print("negative weight cycle is there")
            return
    print(distance)
            
# let directed graph
edges= [[0, 1, -1],[0, 2, 4],[1,2,3],[1, 4, 2],[3, 2, 5],[3, 1, 1],[4, 3, -3]]
BellmanFord(0,edges,5)