import math

def squareArea(side):
    result = side * side
    return result

def rectangleArea(length,width):
    return length * width

def triangleArea(height,base):
    result = (height * base) / 2
    return result

def circleArea(radius):
    return round(math.pi * radius * radius ,2)