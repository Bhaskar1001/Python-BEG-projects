# count down timer

import time

my_time = int(input("enter the time in seconds: "))

for x in range(my_time, 0, -1): #it prints in reverse order or decimal order 0, my_time
    seconds = x % 60
    minutes = int(x / 60) % 60
    hours = int(x / 3600 ) % 24 
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    #time.sleep(1)

print("TIME'S UP")    