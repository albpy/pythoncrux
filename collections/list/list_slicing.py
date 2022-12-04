lst=[10,15,20,25,30,35,40,45,50,55,60,65,70]

#index slicing 
#[start:stop)-->output until (stop-1)

print(lst[2])
print(lst[7])
"""An index to another index(stop-1)"""
print(lst[2:7])
"""An index to end of list)"""
print(lst[3:]) # index 3 to end of list
"""Start of list to an index"""
print(lst[:7]) # index=0 to index=(stop-1)
"""Full Index"""
print(lst[:])
"""An index to another index with step=2"""
print(lst[1:11:2])
"""Start index to end of list with step=3"""
print(lst[1::3])
print(lst[5::2])

print(lst[:4:2]) #index=start=0,stop=4,step=2
print(lst[::4])
