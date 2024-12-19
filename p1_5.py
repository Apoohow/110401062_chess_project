# -*- coding: utf-8 -*-
"""P1_5.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1-UOaGZNZuOmSP0PPCD4dWnODxz9MjRJz
"""

kind=input()
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


if temp_x==0 and temp_y==0:
    print("No")
elif kind=="國王":
    if abs(next_x-now_x)<=1 and abs(next_y-now_y)<=1:
        if checkerboard[next_x][next_y]==1:
            print("No")
        else:
            print("Yes")
    else:
        print("No")
elif kind=="皇后":
    if abs(temp_x)==abs(temp_y):
        for i in range(1,abs(temp_x)+1):
            if next_x>now_x and next_y>now_y:
                if checkerboard[now_x+i][now_y+i]==1:
                    print("No")
                    break
            elif next_x<now_x and next_y>now_y:
                if checkerboard[now_x-i][now_y+i]==1:
                    print("No")
                    break
            elif next_x<now_x and next_y<now_y:
                if checkerboard[now_x-i][now_y-i]==1:
                    print("No")
                    break
            else:
                if checkerboard[now_x+i][now_y-i]==1:
                    print("No")
                    break
            if i==abs(temp_x):
                print("Yes")
    elif abs(temp_x)==0 and abs(temp_y)!=0:
        for i in range(1,abs(temp_y)+1):
            if next_y>now_y:
                if checkerboard[now_x][now_y+i]==1:
                    print("No")
                    break
            else:
                if checkerboard[now_x][now_y-i]==1:
                    print("No")
                    break
            if i==abs(temp_y):
                print("Yes")
    elif abs(temp_x)!=0 and abs(temp_y)==0:
        for i in range(1,abs(temp_x)+1):
            if next_x>now_x:
                if checkerboard[now_x+i][now_y]==1:
                    print("No")
                    break
            else:
                if checkerboard[now_x-i][now_y]==1:
                    print("No")
                    break
            if i==abs(temp_x):
                print("Yes")
    else:
        print("No")
elif kind=="士兵":
    if next_y-now_y==0 and next_x-now_x==1:
        if checkerboard[now_x+1][now_y]==1:
            print("No")
        else:
            print("Yes")
    else:
        print("No")
elif kind=="騎士":
    if temp_x==2 and temp_y==1:
        if next_x>now_x and next_y>now_y:
            if checkerboard[now_x+2][now_y+1]==1:
                print("No")
            else:
                print("Yes")
        elif next_x<now_x and next_y>now_y:
            if checkerboard[now_x-2][now_y+1]==1:
                print("No")
            else:
                print("Yes")
        elif next_x<now_x and next_y<now_y:
            if checkerboard[now_x-2][now_y-1]==1:
                print("No")
            else:
                print("Yes")
        elif next_x>now_x and next_y<now_y:
            if checkerboard[now_x+2][now_y-1]==1:
                print("No")
            else:
                print("Yes")
    elif temp_x==1 and temp_y==2:
        if next_x>now_x and next_y>now_y:
            if checkerboard[now_x+1][now_y+2]==1:
                print("No")
            else:
                print("Yes")
        elif next_x<now_x and next_y>now_y:
            if checkerboard[now_x-1][now_y+2]==1:
                print("No")
            else:
                print("Yes")
        elif next_x<now_x and next_y<now_y:
            if checkerboard[now_x-1][now_y-2]==1:
                print("No")
            else:
                print("Yes")
        elif next_x>now_x and next_y<now_y:
            if checkerboard[now_x+1][now_y-2]==1:
                print("No")
            else:
                print("Yes")
    else:
        print("No")
elif kind=="主教":
    if abs(temp_x)==abs(temp_y):
        for i in range(1,abs(temp_x)+1):
            if next_x>now_x and next_y>now_y:
                if checkerboard[now_x+i][now_y+i]==1:
                    print("No")
                    break
            elif next_x<now_x and next_y>now_y:
                if checkerboard[now_x-i][now_y+i]==1:
                    print("No")
                    break
            elif next_x<now_x and next_y<now_y:
                if checkerboard[now_x-i][now_y-i]==1:
                    print("No")
                    break
            else:
                if checkerboard[now_x+i][now_y-i]==1:
                    print("No")
                    break
            if i==abs(temp_x):
                print("Yes")
    else:
        print("No")
elif kind=="城堡":
    if abs(temp_x)==0 and abs(temp_y)!=0:
        for i in range(1,abs(temp_y)+1):
            if next_y>now_y:
                if checkerboard[now_x][now_y+i]==1:
                    print("No")
                    break
            else:
                if checkerboard[now_x][now_y-i]==1:
                    print("No")
                    break
            if i==abs(temp_y):
                print("Yes")
    elif abs(temp_x)!=0 and abs(temp_y)==0:
        for i in range(1,abs(temp_x)+1):
            if next_x>now_x:
                if checkerboard[now_x+i][now_y]==1:
                    print("No")
                    break
            else:
                if checkerboard[now_x-i][now_y]==1:
                    print("No")
                    break
            if i==abs(temp_x):
                print("Yes")
    else:
        print("No")