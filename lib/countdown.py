# your code goes here!
def countdown(time):
    n = time;
    while n > 0:
        print(f"{n} SECOND(S)!")
        n -= 1
    else:
        print("HAPPY NEW YEAR!")

import time

def countdown_with_sleep(times):
    n = times;
    while n > 0:
        print(f"{n} SECOND(S)!")
        n -= 1
        time.sleep(1)
    else:
        print("HAPPY NEW YEAR!")