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
    