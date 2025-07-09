def find_max(l):
    max = l[0]
    for i in l:
        if max < i:
            max = i
    return max