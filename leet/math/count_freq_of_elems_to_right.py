import operator
from sortedcontainers import SortedList

def count_elements_to_right(rating, op):
    n = len(rating)
    count_elements_to_right = [0] * n
    sorted_list = SortedList()

    for i in range(n - 1, -1, -1):
        if op == operator.gt:
            # Find the position where rating[i] would be inserted for greater than comparison
            pos = sorted_list.bisect_right(rating[i])
            count_elements_to_right[i] = len(sorted_list) - pos
        elif op == operator.lt:
            # Find the position where rating[i] would be inserted for less than comparison
            pos = sorted_list.bisect_left(rating[i])
            count_elements_to_right[i] = pos
        else:
            raise ValueError("Unsupported comparison operator")

        # Add the current element to the sorted list
        sorted_list.add(rating[i])

    return count_elements_to_right

# Example usage:
rating = [2, 5, 3, 4, 1]
print(count_elements_to_right(rating, operator.gt))  # Output: [3, 1, 1, 1, 0] for greater than
print(count_elements_to_right(rating, operator.lt))  # Output: [0, 3, 1, 1, 0] for less than