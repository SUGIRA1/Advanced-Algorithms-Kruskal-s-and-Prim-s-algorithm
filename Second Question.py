from queue import Queue

graph = {
    'a': ['b', 'c'],
    'b': ['d'],
    'c': ['a'],
    'd': ['e'],
    'e': ['d'],
    'f': []
}

visitedNodes = {}  # List for visitedNodes nodes.
queue = Queue()  # Initialize a queue
level = {}
parent = {}
bfs_output = []
weight = 4

for node in graph.keys():
    visitedNodes[node] = False
    parent[node] = None
    level[node] = -1

s = 'a'

visitedNodes[s] = True

level[s] = 0

queue.put(s)


while not queue.empty():
    u = queue.get()
    bfs_output.append(u)

    for v in graph[u]:
        if not visitedNodes[v]:
            visitedNodes[v] = True
            parent[v] = u
            level[v] = level[u] + 1

            queue.put(v)

            for w in level:
                dist = weight * level[v]
            print('Distance from', s, 'to', v, 'is', dist)


print("BFS traversed nodes in this order: ", bfs_output)
