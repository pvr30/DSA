str = "vishal"
print(str[::-1])

def reverse_string(str):
    rev = ""
    for i in str:
        rev = i + rev
    return rev

print(reverse_string(str))