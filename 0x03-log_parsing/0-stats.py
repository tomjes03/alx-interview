#!/usr/bin/python3
"""
Module to parse a log file for statistics
The stdin filestream is read for inputs and metrics are
computed by python
"""

import re
import sys


filesize = 0
errors = ["200", "301", "400", "401", "403", "404", "405", "500"]
error_count = {}
ip_re = "\b([1-9]|[1-9][0-9]|[1][0-9][0-9]|[2][0-4][0-9]|[2][5][0-5])\b\
         .\b([1-9]|[1-9][0-9]|[1][0-9][0-9]|[2][0-4][0-9]|[2][5][0-5])\b\
         .\b([1-9]|[1-9][0-9]|[1][0-9][0-9]|[2][0-4][0-9]|[2][5][0-5])\b\
         .\b([1-9]|[1-9][0-9]|[1][0-9][0-9]|[2][0-4][0-9]|[2][5][0-5])\b\
          - "
datetime_regex = "[\b([1-9][0-9][0-9][0-9])\b-\b([0-9][0-9])\b\
                  -\b([0-9][0-9])\b \b([0-9][0-9])\b:\b([0-9][0-9])\b:\b\
                  ([0-9][0-9])\b.\b([0-9][0-9][0-9][0-9][0-9][0-9])\b] "
url_regex = "\"GET /projects/260 HTTP/1.1\" "
err_regex = "\b([2][0][0]|[3][0][1]|[4][0][0]|[4][0][1]|[4][0][3]|\
             [4][0][4]|[4][0][5]|[5][0][0])\b "
size_regex = "\b([1-9]|[1-9][0-9]|[1-9][0-9][0-9]|[1][0][0-2][0-4])\b"
line_regex = re.compile(r' '.format(ip_re, datetime_regex,
                        url_regex, err_regex, size_regex))
# adjusted the regex, '' and ' ' are different and '' was giving the error
try:
    i = 0
    for line in sys.stdin:
        is_valid = line_regex.search(line)
        # print(is_valid)
        if is_valid:
            i += 1
            stats = line.split(' ')
            # print(stats, len(stats))
            filesize += int(stats[-1])
            if error_count.get(stats[-2]):
                error_count[stats[-2]] += 1
            else:
                error_count[stats[-2]] = 1
            if (i % 10 == 0):
                print('File size: {}'.format(filesize))
                for err in errors:
                    if error_count.get(err):
                        print('{}: {}'.format(err, error_count.get(err)))
except KeyboardInterrupt:
    print('File size: {}'.format(filesize))
    for err in errors:
        if error_count.get(err):
            print('{}: {}'.format(err, error_count.get(err)))
    raise
else:
    print('File size: {}'.format(filesize))
    for err in errors:
        if error_count.get(err):
            print('{}: {}'.format(err, error_count.get(err)))
