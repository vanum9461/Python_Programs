import random
import time
list=[ x for x in range(1,100000)]
set=set(list)
shuf_list=[ x for x in range(1,100000)]
random.shuffle(shuf_list)

s_time=int(time.time()*1000)
for i in shuf_list:
    i in list
e_time=int(time.time()*1000)
r_time=e_time-s_time
print("Time to find {0} elements in list {1} ms".format(len(shuf_list),r_time))

s_time=int(time.time()*1000)
for i in shuf_list:
    i in set
e_time=int(time.time()*1000)
r_time=e_time-s_time
print("Time to find {0} elements in set {1} ms".format(len(shuf_list),r_time))

