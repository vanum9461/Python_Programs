"""from math import *
lat1,long1,lat2,long2=eval(input("Enter the lat and long of two places"))
lat1=radians(lat1)
long1=radians(long1)
lat2=radians(lat2)
long2=radians(long2)

d=3963.0*(acos(sin(lat1)*sin(lat2)+cos(lat1)*cos(lat2)*cos(long1-long2)))
d=d* 1.609344
print(round(d,4))
"""

from math import *
lat1,long1,lat2,long2,lat3,lat4=eval(input("Enter the lat and long of four places"))
lat1=radians(lat1)
long1=radians(long1)
lat2=radians(lat2)
long2=radians(long2)
lat3=radians(lat3)
long3=radians(long3)
lat4=radians(lat4)
long4=radians(long4)
