#!/usr/bin/python3
import sys

stats = {
    '200': 0,
    '301': 0,
    '400': 0,
    '401': 0,
    '403': 0,
    '404': 0,
    '405': 0,
    '500': 0
}

file_size = 0
line_count = 0

def print_stats():
    print("File size: {}".format(file_size))
    for key in sorted(stats.keys()):
        if stats[key]:
            print("{}: {}".format(key, stats[key]))

try:
    for line in sys.stdin:
        try:
            parts = line.split()
            if len(parts) < 9:
                continue
            
            status = parts[-2]
            file_size += int(parts[-1])
            line_count += 1

            if status in stats:
                stats[status] += 1

            if line_count == 10:
                print_stats()
                line_count = 0

        except KeyboardInterrupt:
            print_stats()
            break

    print_stats()

except KeyboardInterrupt:
    print_stats()
