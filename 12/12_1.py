from collections import defaultdict
from queue import SimpleQueue

# input = ["start-A","start-b","A-c","A-b","b-d","A-end","b-end"]
# input = ["dc-end","HN-start","start-kj","dc-start","dc-HN","LN-dc","HN-end","kj-sa","kj-HN","kj-dc"]

with open('input12.txt', 'r') as f:
    input = [x.strip() for x in f.readlines()]

graph = defaultdict(lambda: set())
for connection in input:
    a, b = connection.split('-')
    graph[a].add(b)
    graph[b].add(a)

def already_wisited_small(history, next_node):
    if next_node.isupper(): 
        return False

    return next_node in history

paths = SimpleQueue()
paths.put(['start'])
finished_paths = []

while not paths.empty():
    path = paths.get()

    next_nodes = graph[path[-1]]
    next_nodes = list(filter(lambda x: not already_wisited_small(path, x), next_nodes))

    for next_node in next_nodes:
        new_path = path.copy()
        new_path.append(next_node)
        if next_node == 'end':
            finished_paths.append(new_path)
        else:
            paths.put(new_path)

print(len(finished_paths))
