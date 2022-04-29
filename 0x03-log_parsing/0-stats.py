#!/usr/bin/python3
"""
Module 0-stats
"""
from sys import stdin


file_size = 0
status_code = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
    }


def print_file_size():
    """Prints the file size and status codes"""
    print("File size: {}".format(file_size))

    for k, v in sorted(status_code.items()):
        if v > 0:
            print("{}: {}".format(k, v))


if __name__ == "__main__":
    """Entry point"""

    try:
        for k, in_put in enumerate(stdin, 1):
            try:
                data = in_put.split()
                file_size += int(data[-1])
                if data[-2] in status_code.keys():
                    status_code[data[-2]] += 1

            except ValueError:
                pass

            if not k % 10:
                print_file_size()
    except KeyboardInterrupt:
        print_file_size()
        raise
    print_file_size()
