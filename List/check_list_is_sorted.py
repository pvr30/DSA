# check weather a string is sorted or not

l = [10, 10, 1]

print(sorted(l))  # return a new sorted list
l.sort() # modify/sort the list 


def sorted_or_not(l):
    if len(l) <= 1:
        return 'Yes'
    for i in range(1, len(l)):
        if l[i] < l[i-1]:
            return "No"
        
    return "Yes"

print(sorted_or_not(l))
    

# check if array is sorted incresely or decrisly 
arr1 = [1, 1, 1, 2, 3]
arr2 = [4, 3, 1]

def isSorted(arr,n):
    flag1 = True
    flag2 = True
    for i in range(n-1):
        if arr[i] > arr[i+1] and flag1:
            flag1 = False
        if arr[i] < arr[i+1] and flag2:
            flag2 = False
    
    return int(flag1 or flag2)

print(isSorted(arr1, len(arr1)))
print(isSorted(arr2, len(arr2)))


