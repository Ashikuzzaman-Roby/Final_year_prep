ph,v,s):
#     dist = [float('inf')]*v 
#     par=[-1]*v 
#     heap = []
#     dist[s]=0
#     heapq.heappush(heap,(s,0))
#     while heap:
#         node,dis = heapq.heappop(heap)
#         print(node,dis)
#         for i in graph[node]:
#             n,w=i 
#             new_dis = w+dist[i]
#             print("calculating new distance",new_dis)
#             if new_dis<dist[i]:
#                 dist[i]=new_dis 
#                 print(new_dis)
#                 par[i]=node 
#                 heapq.heappush(heap,(i,dist[i]))
#     print("val",dist)
#     print(par)
# find_shortest_path(graph,v,0)