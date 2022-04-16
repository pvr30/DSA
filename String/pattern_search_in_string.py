str = "data sturcture and alogrithm and python"

def find_pattern(str, pat):
    pos = str.find(pat)
    while pos >= 0:
        print(pos)
        pos = str.find(pat, pos+1)
        

# find_pattern(str, "data")
find_pattern(str, "and")
find_pattern(str, "python")
