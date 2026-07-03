# https://leetcode.com/problems/unique-binary-search-trees

class Solution:
    def numTrees(self, n: int) -> int:
        # pretty unique question
        
        # [1,2,3,4,5]
        # treat each node as the root
        # catalan numbers pop up

        # ways[i] = ways to make distinct bst with i nodes
        ways = [0 for _ in range(n+1)] 
        ways[0] = 1

        for num_nodes in range(1, n+1):
            for root in range(1, n+1):
                left_size = root-1
                right_size = num_nodes-root
                ways[num_nodes] += ways[left_size]*ways[right_size] # each tree on the left can be match with each tree on the right
                
        return ways[n]