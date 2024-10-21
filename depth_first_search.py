# pseudocode
# DFS (G, u)
# u.visited = true
# for each v adjacent to u
#   if visited is false, call DFS(G,v)
# main fxn
# for each node in Graph, set visited to false
# for each node in graph, call DFS(G,v)

def dfs(visited, graph, node):
    stack = []
    stack.append(node)
    visited = set()
    while stack:
        v = stack.pop()
        if v not in visited:
            print (v, end=" ")
            visited.add(v)
            for node in graph[v]:
                stack.append(node)

def dfs_recursive(visited, graph, node):
    if node not in visited:
        print (node, end=" ")
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

graph = {
  'A' : ['B','C'],
  'B' : ['D', 'E'],
  'C' : ['F'],
  'D' : [],
  'E' : ['F'],
  'F' : []
}

visited = []
visited_rec = set() 
dfs(visited, graph, 'A')
print()
dfs_recursive(visited_rec, graph, 'A')