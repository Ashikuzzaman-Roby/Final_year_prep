# trying for dijkastra's algo and A* Search : 


# first I am trying to recall Heapque or priority que  :

import heapq
heap =[]
lst=[223,223,334,335,6,7,8]
for i in range(len(lst)):
    heapq.heappush(heap,{i,lst[i]})
    # print(heap)
print(heap)

while heap:
    node, dist=heapq.heappop(heap)
    print(f"{node} : {dist}")







# making a graph :
v=6
edges =[(0,2,4),(0,1,4),(1,2,2),(2,3,3),(2,5,6),(2,4,1),(3,5,2),(4,5,3)]
def making_graph(v,edges):
    graph =[[] for _  in range(v)]
    for i in edges:
        u,v,w=i 
        graph[u].append((v,w))
        graph[v].append((u,w))
    return graph
graph = making_graph(6,edges)
print(graph)
print("next print starts from here : ")

import heapq
def finding_shortest_path(graph,s,v):
    par = [-1]*v 
    dist = [float("inf")]*v
    heap = []
    heapq.heappush(heap,(0,s))
  
    dist[s]=0
    
    while heap :
        dis ,node= heapq.heappop(heap)
        print(node,dis)
        for n,d in graph[node]: 
            if d+dist[node]<dist[n]:
                par[n]=node 
                dist[n]= d+dist[node]
                heapq.heappush(heap,(d+dist[node],n))
    print("parent : ",par)
    print("distance : " , dist)


finding_shortest_path(graph,0,v)

