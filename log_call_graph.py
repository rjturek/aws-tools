# Debug, dump package locations
# import site
# print(site._init_pathinfo())

from process_log import rand_log
import sys
import io

import time

def follow(thefile):
    # thefile.seek(0,2)      # Go to the end of the file
    while True:
        line = thefile.readline()
        if not line:
            time.sleep(0.1)    # Sleep briefly
            continue
        yield line

# Example use
if __name__ == '__main__':
    out_stream = io.StringIO()
    random_logger1 = rand_log.RandomLogger(out_stream=out_stream)
    random_logger1.gen_log()
    print(out_stream.getvalue())
