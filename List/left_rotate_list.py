# left rotate a list 

l = [10, 20, 30, 40]

print(l[1:] + l[0:1])  # method 1

l.append(l.pop(0)) # method 2
print(l)

new_l = [1, 2, 3, 4]

def left_rotate(l):
    n = len(l)
    x = l[0]
    for i in range(1, n):
        l[i-1] = l[i]
    l[n-1] = x

left_rotate(new_l)
print(new_l)