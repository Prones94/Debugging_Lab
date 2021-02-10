import math
​
def get_distance_btwn_circles(self):
    # Calculate the distance between the two circles
    xc1 = 4
    yc1 = 4.25
​
    xc2 = 53
    yc2 = -5.35
​
    distance = math.sqrt((xc1-xc2)**2 + (yc1 - yc2)**2)
    print('distance', distance)
​
# *** somewhere else in your program ***
​
def get_vector_len(self):
    # Calcualte the length of vector AB vector which is a vector between A and B points.
    xa = -36
    ya = 97
​
    xb = .34
    yb = .91

    length = math.sqrt((xa-xb)*(xa-xb) + (ya-yb)*(ya-yb))
    print('length', length)
