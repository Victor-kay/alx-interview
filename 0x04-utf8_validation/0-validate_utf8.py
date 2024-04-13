#!/usr/bin/python3
"""
Module to determine if a given data set represents a valid UTF-8 encoding.
"""


def validUTF8(data):
    """
    Determines if data is a valid UTF-8 encoding.
    
    Args:
        data (list): A list of integers representing bytes of data.
        
    Returns:
        bool: True if data is a valid UTF-8 encoding, else False.
    """
    num_follow_bytes = 0
    
    for byte in data:
        if num_follow_bytes:
            if byte >> 6 != 0b10:
                return False
            num_follow_bytes -= 1
        else:
            if byte >> 7 == 0b0:
                continue
            elif byte >> 5 == 0b110:
                num_follow_bytes = 1
            elif byte >> 4 == 0b1110:
                num_follow_bytes = 2
            elif byte >> 3 == 0b11110:
                num_follow_bytes = 3
            else:
                return False
    return num_follow_bytes == 0


# For testing
if __name__ == "__main__":
    test_cases = [
        ([467, 133, 108], True),
        ([240, 188, 128, 167], True),
        ([235, 140], True),
        ([345, 467], False),
        ([250, 145, 145, 145, 145], True),
        ([0, 0, 0, 0, 0, 0], False),
        ([], True)
    ]

    for data, expected in test_cases:
        result = validUTF8(data)
        print(f"Data: {data}, Got: {result}, Expected: {expected}")
