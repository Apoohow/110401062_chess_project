# -*- coding: utf-8 -*-
"""P1_3.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1blOzoKds-e1AloPBjtLuVKGQvLOeKenU
"""

now=input().split(" ")
now_x=int(now[0])
now_y=int(now[1])
nextp=input().split(" ")
next_x=int(nextp[0])
next_y=int(nextp[1])

# checkerboard=[[0]*8 for i in range(8)]
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




if next_y-now_y==0 and next_x-now_x==1:
    if checkerboard[now_x+1][now_y]==1:
        print("No")
    else:
        print("Yes")
else:
    print("No")