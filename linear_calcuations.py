"""
Name:William Nathan
Date: 12/16/24
Description: Slope project
"""

def slope(point1:tuple,point2:tuple)->float:
    rise = float(point1[1]-point2[1])
    run = float(point1[0]-point2[0])
    slope = rise/run
    return slope

def distance(point1:tuple, point2:tuple)->float:
    distance = float(point2[0]-point1[0])
    return distance

def main():
    print(slope((1,1),(2,2)))
    print(distance((1,1),(2,2)))


if __name__ == "__main__":
    main()