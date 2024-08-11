# example code for tarjans algo to gen SSCs
# does so by finding articulation points
def tarjan_scc(graph):
    index = 0
    stack = []
    indices = {}
    lowlink = {}
    on_stack = {}
    sccs = []

    def strongconnect(v):
        nonlocal index
        indices[v] = index
        lowlink[v] = index
        index += 1
        stack.append(v)
        on_stack[v] = True

        for w in graph[v]:
            if w not in indices:
                strongconnect(w)
                lowlink[v] = min(lowlink[v], lowlink[w])
            elif on_stack[w]:
                lowlink[v] = min(lowlink[v], indices[w])

        if lowlink[v] == indices[v]:
            scc = []
            while True:
                w = stack.pop()
                on_stack[w] = False
                scc.append(w)
                if w == v:
                    break
            sccs.append(scc)

    for v in graph:
        if v not in indices:
            strongconnect(v)

    return sccs

# Example usage:
graph = {
    'A': ['B'],
    'B': ['C', 'E'],
    'C': ['F'],
    'D': ['A'],
    'E': ['D'],
    'F': ['C'],
    'G': []
}

print(tarjan_scc(graph))