class Solution:
    def maximumValueSum(self, nums: list[int], k: int, edges: list[list[int]]) -> int:
        # all nodes can reach each other (double edged tree)
        # can pick any pair of nodes, dont need to be adjacent
        # give each node a score
        # pick out the top scores

        state_B = []
        # assign the score for each node
        for i, num in enumerate(nums):
            state_B.append(num ^ k)
        
        state_A = nums
        elems = sorted(zip(state_A, state_B), key=lambda x: x[1] - x[0], reverse=True)
        # pick out best options
        # 2 states, A and B
        # pick elems and choose their state to max score
        # but we can only make elems into state B by pairs
        total = 0
        i = 0
        # judge by pairs, transform or not
        while i < len(elems) - 1:
            a = elems[i]
            b = elems[i + 1]
            state_a_score = a[0] + b[0]
            state_b_score = a[1] + b[1]

            if state_a_score >= state_b_score:
                total += a[0] # dont transform
                i += 1
            else:
                total += a[1] + b[1] # transform
                i += 2

        # add odd one out
        if len(elems) % 2 != 0:
            total += elems[-1][0] # state_a of left out elem
        elif i == len(elems) - 1: # ends with 2 state_a, take the last one too
            total += elems[-1][0]

        return total