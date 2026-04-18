# https://leetcode.com/problems/construct-smallest-number-from-di-string

class Solution:
    # NOTE: there is also a O(n) greedy solution

    # O(n!)
    def smallestNumber(self, pattern: str) -> str:
        
        # pattern = "IIIDIDDD"
        # Output:   "123549876"

        def bt(i, builder):
            nonlocal smallest
            if i >= len(pattern):
                smallest = ''.join([str(c) for c in builder])
                return True
            
            for num in sorted(options):
                if i == 0:
                    builder.append(num)
                    options.remove(num)
                    if bt(i + 1, builder):
                        return True
                    builder.pop()
                    options.add(num)
                elif (pattern[i - 1] == 'I' and builder[-1] < num or
                pattern[i - 1] == 'D' and builder[-1] > num):
                    builder.append(num)
                    options.remove(num)
                    if bt(i + 1, builder):
                        return True
                    builder.pop()
                    options.add(num)

            return False

        options = set([num for num in range(1, 10)])
        smallest = ''
        pattern = pattern + 'D' # add an arbitrary char to make the algo meet the constraint of the last char
        bt(0, [])
        return smallest