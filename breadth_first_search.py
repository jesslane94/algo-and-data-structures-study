# pseudocode
# create a queue
# mark v as visited and put in queue
# while q is not empty:
# remove the head (u) of queue
# mark and enqueue all (unvisited) neighbors of u

def bfs(visited, graph, node):
    queue = []
    visited.append(node)
    queue.append(node)

    while queue:
        v = queue.pop(0)
        print(v, end=" ")

        for neighbor in graph[v]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)

graph = {
  'A' : ['B','C'],
  'B' : ['D', 'E'],
  'C' : ['F'],
  'D' : [],
  'E' : ['F'],
  'F' : []
}

visited = []
bfs(visited, graph, 'A')