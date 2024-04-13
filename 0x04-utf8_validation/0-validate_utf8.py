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
    
    # Helper function to check if a byte starts with '10'
    def is_follow_byte(byte):
        return byte & 0b11000000 == 0b10000000
    
    # Check the number of follow bytes for each byte in data
    num_follow_bytes = 0
    
    for byte in data:
        # If there are follow bytes expected but the current byte doesn't start with '10'
        if num_follow_bytes:
            if not is_follow_byte(byte):
                return False
            num_follow_bytes -= 1
        else:
            # Determine the number of follow bytes from the current byte
            mask = 0b10000000
            while mask & byte:
                num_follow_bytes += 1
                mask >>= 1
            
            # Single byte character
            if num_follow_bytes == 1 or num_follow_bytes > 3:
                return False
                
            # If there are no follow bytes expected, but the byte starts with '10'
            if num_follow_bytes == 0 and is_follow_byte(byte):
                return False
            
            # Decrement num_follow_bytes to account for the current byte
            num_follow_bytes -= 1
            
    # If there are still follow bytes expected but the data ends prematurely
    if num_follow_bytes:
        return False
    
    return True

# For testing
if __name__ == "__main__":
    data = [65]
    print(validUTF8(data))  # True

    data = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
    print(validUTF8(data))  # True

    data = [229, 65, 127, 256]
    print(validUTF8(data))  # False
