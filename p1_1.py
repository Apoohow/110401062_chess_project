# -*- coding: utf-8 -*-
"""P1_1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/10MKqAK4VfsFR0-blMz4DxnrUjdJEALwl
"""

now=input().split(" ")
now_x=int(now[0])
now_y=int(now[1])
nextp=input().split(" ")
next_x=int(nextp[0])
next_y=int(nextp[1])

#checkerboard=[[0]*8 for i in range(8)]
# checkerboard=[ [1, 0, 0, 0, 0, 0, 0, 0],
#   [0, 0, 0, 0, 0, 0, 0, 0],
#   [0, 0, 1, 0, 0, 0, 0, 0],
#   [0, 0, 0, 0, 0, 0, 0, 0],
#   [0, 0, 0, 0, 0, 0, 0, 0],
#   [0, 0, 0, 0, 0, 0, 0, 0],
#   [0, 0, 0, 0, 0, 0, 0, 0],
#   [0, 0, 0, 0, 0, 0, 0, 0] ]
checkerboard[now_x][now_y]=1

temp_x=abs(next_x-now_x)
temp_y=abs(next_y-now_y)


if temp_x==0 and temp_y==0:
    print("No")

if abs(next_x-now_x)<=1 and abs(next_y-now_y)<=1:
    if checkerboard[next_x][next_y]==1:
        print("No")
    else:
        print("Yes")
else:
    print("No")