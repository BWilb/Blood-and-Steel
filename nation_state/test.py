import sys
import time
def slower(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.19)
slower("hello world")