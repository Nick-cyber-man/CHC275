def linearsearch(list,target):
    curr = 0
    for i in range(len(list)):
        curr = i
        if list[i] == target:
            return i,curr
    return "not found"

def nested(n):
    for i in range(n):
        for j in range(n):
            print(i,j)

def binarysearch(list,target,curr_item):
    mid = len(list)/2
    if list[mid] == target:
        return target,curr_item
    
    if list[mid] < target:
        return binarysearch(list(mid),target,curr_item + 1)
    if list[mid] > target:
        return binarysearch(list(mid),target,curr_item + 1)
    
def foo(n):
    print("while")
    
    
print(5*4*3*2*1* > 3*2)
    
##nested(2) puts things to the power