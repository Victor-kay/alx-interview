#!/usr/bin/python3

def canUnlockAll(boxes):
    if not boxes:
        return False

    # Initialize a set to keep track of visited boxes
    visited = set()

    # Initialize a queue for BFS traversal
    queue = [0]

    # Mark the first box as visited
    visited.add(0)

    # Perform BFS traversal
    while queue:
        current_box = queue.pop(0)
        for key in boxes[current_box]:
            if key < len(boxes) and key not in visited:
                visited.add(key)
                queue.append(key)

    # If all boxes have been visited, return True
    return len(visited) == len(boxes)

if __name__ == "__main__":
    boxes1 = [[1], [2], [3], [4], []]
    print(canUnlockAll(boxes1))  # Output: True

    boxes2 = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
    print(canUnlockAll(boxes2))  # Output: True

    boxes3 = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
    print(canUnlockAll(boxes3))  # Output: False
