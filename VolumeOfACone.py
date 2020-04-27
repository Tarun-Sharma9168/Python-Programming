import math
def cone_volume(h, r):
    return (1/3*math.pi * (r**2) * h)
print(round(cone_volume(3,2),2))
print(round(cone_volume(15,6),2))
print(round(cone_volume(18,0),2))
     
	