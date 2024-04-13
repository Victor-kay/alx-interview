#!/usr/bin/python3
import sys
import re

def print_stats(file_sizes, status_codes):
    """
    Print statistics including total file size and number of lines by status code.

    Args:
    - file_sizes (list): List of file sizes from the log entries.
    - status_codes (dict): Dictionary containing counts of each status code.

    Returns:
    - None
    """
    total_size = sum(file_sizes)
    print("File size: {:d}".format(total_size))

    sorted_codes = sorted(status_codes.keys())
    for code in sorted_codes:
        if status_codes[code] > 0:
            print("{}: {:d}".format(code, status_codes[code]))

def main():
    """
    Main function to read log entries from stdin and compute statistics.

    Reads log entries line by line from stdin.
    Computes statistics for total file size and number of lines by status code.
    Prints statistics after every 10 lines or a keyboard interruption.

    Returns:
    - None
    """
    file_sizes = []
    status_codes = {
        '200': 0,
        '301': 0,
        '400': 0,
        '401': 0,
        '403': 0,
        '404': 0,
        '405': 0,
        '500': 0
    }
    count = 0

    try:
        for line in sys.stdin:
            count += 1
            match = re.match(r"^\d+\.\d+\.\d+\.\d+ - \[.*\] \"GET /projects/260 HTTP/1\.1\" (\d+) (\d+)$", line.strip())
            if match:
                status_code, file_size = match.groups()
                status_code = status_code.strip()
                file_size = int(file_size.strip())

                if status_code in status_codes:
                    status_codes[status_code] += 1
                file_sizes.append(file_size)

            if count == 10:
                print_stats(file_sizes, status_codes)
                count = 0

        if file_sizes:
            print_stats(file_sizes, status_codes)

    except KeyboardInterrupt:
        print_stats(file_sizes, status_codes)

if __name__ == "__main__":
    main()
