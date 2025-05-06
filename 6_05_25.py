'Patterns'
'EX:1'
# n=5
# for x in range(1,n+1):
#     for y in range(1,n+1):
#         print('* ',end="")
#     print()

"EX:2 ==> Right Angle Triangle"
# n=5
# for x in range(1,n+1):
#     for y in range(1,x+1):
#         print('* ',end="")
#     print()

"EX:3 Left Angle Triangle"
# n=5
# for x in range(1,n+1):
#     for y in range(n-x):
#         print(' ',end="")
#     for c in range(1,x+1):
#         print('*',end="")
#     print()

"Another Method"
# n=5
# for x in range(1,n+1):
#     print(" "*(n-x),"*"*x,end=" ")
#     print()

"EX:4"
# n=5
# for x in range(1,n+1):
#     for y in range(1,x+1):
#         print(y,end=" ")
#     print()

"Ex:5"
# n=5
# for x in range(1,n+1):
#     for c in range(1,x+1):
#         print(x,end="")
#     print()

"EX:6"
# n=5
# for x in range(n,0,-1):
#     for c in range(1,x+1):
#         print('*',end="")
#     print()

"Ex:6"

# n=5
# for x in range(n,0,-1):
#     for y in range(1,x+1):
#         print(y,end=" ")
#     print()

"EX:7 Triangle"
# n=5
# for x in range(1,n+1):
#     for y in range(n-x):
#         print(' ',end="")
#     for t in range(1,x+1):
#         print('* ',end="")
#     print()

"EX:8 Reverse Triangle"
# n=5
# for x in range(n,0,-1):
#     for y  in range(n-x):
#         print(' ',end="")
#     for c in range(1,x+1):
#         print('* ',end="")
#     print()

"EX:9"
# n=5
# for x in range(1,n+1):
#     for y in range(n-x):
#         print(' ',end="")
#     for t in range(1,x+1):
#         print('* ',end="")
#     print()
# for x in range(n,0,-1):
#     for y  in range(n-x):
#         print(' ',end="")
#     for c in range(1,x+1):
#         print('* ',end="")
#     print()

"EX:10 ==>A"
'rows=5'
'colums=3'
# for rows in range(1,5):
#     for column in range(1,4):
#         if rows==1 or rows==3:
#             print('* ',end="")
#         elif (rows==2 and column==1 or column==3) or (rows==4 and column==1 or column==3) or (rows==4 and column==1 or column==3):
#             print('* ',end=" ")
#         else:
#             print(' ',end="")
#     print()



"EX:11"
# n=5
# for x in range(1,n+1):
#     for y in range(n-x):
#         print("",end="")
#     for c in range(1,x+1):
#         print('*',end=" ")
#     print()
# for x in range(n-1,0,-1):
#     for y in range(n-x):
#         print("",end="")
#     for c in range(1,x+1):
#         print('*',end=" ")
#     print()

"EX:12"
# n=15
# p=5
# for x in range(1,p+1):
#     for y in range(1,x+1):
        