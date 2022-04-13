# left rotate k times
 
l = [10, 20, 30, 40]
k = 2
print(l[k:] + l[0:k]) 


new_l = [1, 2, 3, 4]

def left_rotate_k_times(l, k):
    while k:
        n = len(l)
        x = l[0]
        for i in range(1, n):
            l[i-1] = l[i]
        l[n-1] = x
        k -= 1

left_rotate_k_times(new_l, 3)
print(new_l)