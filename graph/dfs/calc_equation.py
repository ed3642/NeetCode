from collections import defaultdict

class Solution:
    def calcEquation(self, equations: list[list[str]], values: list[float], queries: list[list[str]]) -> list[float]:
        # reverse all known edges with 1/weight
        # dfs with a running multiplication from source -> dest for each query
        # can keep track of known calculations

        def dfs(source, node, target, running_mult, visited):
            visited.add(node)

            for neighbor_node, neighbor_weight in adj_list[node]:
                if neighbor_node not in visited:
                    new_mult = running_mult * neighbor_weight
                    if neighbor_node == target:
                        adj_list[node].append((neighbor_node, new_mult))
                        adj_list[neighbor_node].append((node, 1 / new_mult))
                        known_solutions[(source, neighbor_node)] = new_mult
                        known_solutions[(neighbor_node, source)] = 1 / new_mult
                        return new_mult
                    result = dfs(source, neighbor_node, target, new_mult, visited)
                    if result:
                        return result

        adj_list = defaultdict(list)
        known_solutions = defaultdict(float)
        n = len(equations)

        for i in range(n):
            _from, to = equations[i]
            weight = values[i]
            adj_list[_from].append((to, weight))
            # adding reversed known edges
            adj_list[to].append((_from, 1 / weight))
            known_solutions[(_from, to)] = weight
            known_solutions[(to, _from)] = 1 / weight
        
        res = []
        for _from, to in queries:
            if (_from, to) in known_solutions:
                res.append(known_solutions[(_from, to)])
                continue
            
            if (_from or to) not in adj_list:
                res.append(-1.0)
            elif _from == to:
                res.append(1.0)
            else:
                q_result = dfs(_from, _from, to, 1, set())
                if q_result:
                    res.append(q_result)
                else:
                    res.append(-1.0)
        return res
