import heapq

def network_delay_time(times, N, K):

    graph = {i: [] for i in range(1, N + 1)}
    
    for u, v, w in times:
        graph[u].append((v, w))
    
    min_heap = [(0, K)]

    distance = {i: float('inf') for i in range(1, N + 1)}
    distance[K] = 0
    
    while min_heap:
        curr_time, node = heapq.heappop(min_heap)
        
        if curr_time > distance[node]:
            continue
        
        for neighbor, travel_time in graph[node]:
            time = curr_time + travel_time
            if time < distance[neighbor]:
                distance[neighbor] = time
                heapq.heappush(min_heap, (time, neighbor))
    
    max_time = max(distance.values())
    
    return max_time if max_time < float('inf') else -1

N = int(input("Enter the number of nodes: "))
M = int(input("Enter the number of edges: "))

times = []
print("Enter the edges in the format 'ui vi wi' (one per line):")
for i in range(M):
    u, v, w = map(int, input().split())
    times.append((u, v, w))

K = int(input("Enter the starting node (K): "))

result = network_delay_time(times, N, K)
print("The time taken for the signal to reach all nodes:", result)  
