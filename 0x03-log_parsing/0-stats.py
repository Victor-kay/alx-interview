#!/usr/bin/python3
"""
Log parsing script to compute metrics from log lines.
"""

import sys

def print_metrics(total_size, status_codes):
    """Print metrics from the beginning"""
    print("File size: {:d}".format(total_size))
    sorted_codes = sorted(status_codes.keys())
    for code in sorted_codes:
        print("{:d}: {:d}".format(code, status_codes[code]))

def parse_line(line, total_size, status_codes):
    """Parse a single log line"""
    try:
        parts = line.split()
        if len(parts) < 9 or parts[5] != "\"GET" or parts[6] != "/projects/260":
            return total_size, status_codes
        
        status_code = int(parts[-2])
        file_size = int(parts[-1])
        
        if status_code in [200, 301, 400, 401, 403, 404, 405, 500]:
            status_codes[status_code] = status_codes.get(status_code, 0) + 1
        
        total_size += file_size
        return total_size, status_codes
    
    except ValueError:
        return total_size, status_codes

def main():
    """Main function to read and parse log lines"""
    total_size = 0
    status_codes = {}
    
    try:
        for line in sys.stdin:
            line = line.strip()
            if not line:
                continue
            
            total_size, status_codes = parse_line(line, total_size, status_codes)
        
        print_metrics(total_size, status_codes)
            
    except KeyboardInterrupt:
        print_metrics(total_size, status_codes)

if __name__ == "__main__":
    main()
