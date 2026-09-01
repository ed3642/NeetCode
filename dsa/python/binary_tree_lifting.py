import math

n = 10
LOG = int(math.log2(n)) + 2 # where n is the dataset size

# LCA of a treenode by binary lifting
def lca(u, v, parent, depth):
    # lift deeper node
    if depth[u] < depth[v]:
        u, v = v, u

    diff = depth[u] - depth[v]
    for k in range(LOG):
        if diff & (1 << k):
            u = parent[k][u]

    if u == v:
        return u

    # lift both until parents match
    for k in reversed(range(LOG)):
        if parent[k][u] != parent[k][v]:
            u = parent[k][u]
            v = parent[k][v]

    return parent[0][u]