import numpy as np
#Sort function in numpy

sorting_mat=np.array([2,7,5,4,0,9])
print(sorting_mat)

#Order in ascending order
ascen=np.sort(sorting_mat)
print(ascen)
dscent=np.sort(sorting_mat)[::-1]
print(dscent)
#Sorting in descending

srt2D=np.array([[2,3,4,6],[3,3,7,1],[4,5,8,3],[4,2,7,6]])
print(srt2D)
print(np.sort(srt2D))#row wise sort/axis=1
print(np.sort(srt2D,axis=0)) #colomn wise sort
"""look 2D descending array"""
#-------------------------------argsort()--------------------------------
c=np.argsort(sorting_mat)#sort based on index value
print(c)    #[0,1,2,3,4,5]
            #2-->0
            #7-->1
            #5-->2
            #4-->3
            #0-->4
            #9-->5 ==>[4,0,3,2,1,5]
"""2D Rowwise"""
d=np.argsort(srt2D) #[2,3,4,6]-->[2,3,4,6]==>[0,1,2,3]
print(d)            #[3,3,7,1]-->[1,3,3,7]==>[3,0,1,3]
                    #[4,5,8,3]-->[3,4,5,8]==>[3,0,1,2]
                    #[4,2,7,6]-->[2,4,6,7]==>[1,0,3,2]
"""2D Colomnwise--------"""

e=np.argsort(srt2D, axis=0)
print(e)
                    #[2,3,4,6]-->[2,2,4,1]==>[0,3,0,1]
                    #[3,3,7,1]-->[3,3,7,3]==>[1,0,1,2]
                    #[4,5,8,3]-->[4,3,7,6]==>[2,1,3,0]
                    #[4,2,7,6]-->[4,5,8,6]==>[3,2,2,3]

print(np.max(srt2D))
print(np.argmax(srt2D))
print(np.max(srt2D,axis=0))#colomnwise
print(np.argmax(srt2D,axis=0))


print(np.min(srt2D))
print(np.argmin(srt2D))
print(np.min(srt2D,axis=0))
print(np.argmin(srt2D,axis=0))
