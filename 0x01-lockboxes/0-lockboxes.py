#!/usr/bin/python3

def canUnlockAll(boxes):
    # Set to store keys we have
    keys = set([0])  # We start with the key to the first box
    # Set to store boxes we can open
    openable_boxes = set([0])

    while openable_boxes:
        # Pop a box from the set of openable boxes
        box = openable_boxes.pop()
        # Get keys in the current box
        box_keys = boxes[box]

        # Try to open all the boxes with the keys we have
        for key in box_keys:
            if key not in keys:
                # If we haven't used this key before, add it to keys
                keys.add(key)
                # Add the box corresponding to this key to openable_boxes
                openable_boxes.add(key)

    # If all boxes have been opened, return True
    return len(keys) == len(boxes)

# Testing the function
if __name__ == "__main__":
    boxes1 = [[1], [2], [3], [4], []]
    print(canUnlockAll(boxes1))  # Output: True

    boxes2 = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
    print(canUnlockAll(boxes2))  # Output: True

    boxes3 = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
    print(canUnlockAll(boxes3))  # Output: False
