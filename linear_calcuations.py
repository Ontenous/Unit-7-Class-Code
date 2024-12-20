"""
Name:William Nathan
Date: 12/16/24
Description: Slope project
"""
import math

def slope(point1:tuple,point2:tuple)->float:
    rise = float(point2[1]-point1[1])
    run = float(point2[0]-point1[0])
    slope = rise/run
    return slope

def distance(point1:tuple, point2:tuple)->float:
    deltax = float(point2[0]-point1[0])
    deltay = float(point2[1]-point1[1])
    pythag = math.sqrt((deltay*deltay) + (deltax*deltax))
    return pythag

def main():
    print(slope((1,1),(2,2)))
    print(distance((1,1),(2,2)))


if __name__ == "__main__":
    main()