from datetime import time
from time import sleep

print('Please, insert time to count down (h : m : s) ex. 00 : 00 : 00')
h = int(input())
m = int(input())
s = int(input())
t = (h * 3600) + (m * 60) + s
while  t != 0:
    print(time(hour = t // 3600, minute = (t % 3600) // 60, second = t % 60 ))
    sleep(1)
    t -= 1