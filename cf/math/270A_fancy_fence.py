#!/usr/bin/env python3
# PowerShell:  gc input.txt | python main.py

from math import sin, cos, pi
import sys
input = sys.stdin.readline

INF = float('inf')
def rint(): return int(input())
def rints(): return list(map(int, input().split()))
def rchars(): return list(input().strip())
def rstring(): return input().strip()
def rintiter(): return map(int, input().split())
def read_all(): return sys.stdin.read().split('/n')

def solve(a):
    # we can also solve it by rotating the vector [1, 0] by 180-a deg and seeing it returns to [1, 0] by at most 360 degrees. Not as fast but thought it was interesting solution.

    # Ta=w until past 360 deg
    # after multiplying the rotation matrix by [1, 0] we see that w = [cos(theta), -sin(theta)]
    # so if that x component ever becomes 1 again it lands on the same position in the accepted num of transformations
    max_transformations = (360//(180-a))
    err = 10**-5

    theta = (180-a) * (pi/180) # convert to rads
    x = 1
    y = 0
    for _ in range(max_transformations):
        nx = x*cos(theta)-y*sin(theta)
        ny = y*cos(theta)+x*sin(theta)
        if abs(1.0-nx) <= err and abs(ny) <= err:
            return 'YES'
        x = nx
        y = ny
    return 'NO'

def solve2(a):
    # 60
    # 90
    # inner angle sum = 180(n-2) where 'n' is the number of faces of polygon
    # with sum = n*a where 'a' is the angle given
    # we can derive n = 360/(180-a) and 'n' must be an int
    return 'YES' if 360%(180-a) == 0 else 'NO'

def main():
    res = []

    t = rint()
    for _ in range(t):
        res.append(solve(rint()))
            
    print('\n'.join(map(str, res)))

if __name__ == "__main__":
    main()
