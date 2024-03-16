#!/usr/bin/python3
"""
Determines if all the boxes can be opened.
"""


def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened.

    Args:
        boxes (list of lists): A list of lists where each inner list represents a box
            and contains keys to other boxes.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    if not boxes:
        return False

    n = len(boxes)
    keys = set(boxes[0])
    visited = {0}  # Set to store visited boxes

    while keys:
        key = keys.pop()

        if key < n and key not in visited:
            keys.update(boxes[key])
            visited.add(key)

    return len(visited) == n


# Test cases
if __name__ == "__main__":
    boxes1 = [[1], [2], [3], [4], []]
    print(canUnlockAll(boxes1))  # Output: True

    boxes2 = [[1, 4, 5], [2], [5, 2], [3], [4, 1], [3, 5]]
    print(canUnlockAll(boxes2))  # Output: True

    boxes3 = [[4, 6], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
    print(canUnlockAll(boxes3))  # Output: False
