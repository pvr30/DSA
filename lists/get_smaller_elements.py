def get_smaller_elements_list(l, x):
    smaller_list = [ele for ele in l if x > ele]
    return smaller_list

if __name__ == "__main__":
    l = get_smaller_elements_list([10, 12, 14, 15], 13)
    print(l)
