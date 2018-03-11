def prod_3num(alist):
    if len(alist) < 3:
        return False
    max_list = []
    min_list = []
    alist.sort()
    i = 0
    while i < 3:
        max_list.append(alist.pop())
        min_list.append(alist.pop(0))
        i = i + 1
    min_list = min_list[:2] + [max_list[0]]
    maximum = 1
    minimum = 1
    for max_list_elem in max_list:
        maximum = maximum*max_list_elem
    for min_list_elem in min_list:
        minimum = minimum*max_list_elem
    if maximum>minimum:
        return maximum
    return minimum


print (prod_3num([100, -11, 1234, 1324, 1432, 3423, -9812, -59887, 6412]))

