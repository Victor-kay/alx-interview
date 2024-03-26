#!/usr/bin/python3
import sys
import re
from collections import defaultdict

def print_statistics(total_size, status_counts):
    print("File size:", total_size)
    for status_code in sorted(status_counts.keys()):
        print(f"{status_code}: {status_counts[status_code]}")

def parse_line(line):
    match = re.match(r'^\d+\.\d+\.\d+\.\d+ - \[(.*?)\] "GET /projects/260 HTTP/1\.1" (\d+) (\d+)$', line)
    if match:
        status_code = int(match.group(2))
        file_size = int(match.group(3))
        return status_code, file_size
    return None

def main():
    total_size = 0
    status_counts = defaultdict(int)
    try:
        for i, line in enumerate(sys.stdin, start=1):
            parsed = parse_line(line.strip())
            if parsed:
                status_code, file_size = parsed
                total_size += file_size
                status_counts[status_code] += 1
            if i % 10 == 0:
                print_statistics(total_size, status_counts)
    except KeyboardInterrupt:
        print_statistics(total_size, status_counts)

if __name__ == "__main__":
    main()
