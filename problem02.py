# def sum(integer):
#     store = 0
#     for i in integer:
#         store =store + i
#     return store

# def square(a):
#     return a * a

# def cube(x):
#     return x * x * x

# def splitsum(l):
#     pos = []
#     neg = []
#     for i in range(len(l)):
#         if l[i] >= 0:
#             pos.append(square(l[i]))
#         else:
#             neg.append(cube(l[i]))  
#     return ([sum(pos), sum(neg)])

# l=[-1,2,3,-7]
# print(splitsum(l))    
####################################################################################################################
####################################################################################################################
####################################################################################################################
#::::::::::: modified program:::::::
# def splitsum(l):
#     pos=0
#     neg=0
#     for n in l:
#         if n>0:
#             pos=pos+n**2  
#         else :
#             neg=neg+n**3
#     return([pos,neg]) 
# l=[-1,2,3,-7]
# print(splitsum(l)) 