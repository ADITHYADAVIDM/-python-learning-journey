n = int(input("Enter the number of elements : "))
l = []
for i in range(n):
    l.append(int(input("Enter element : ")))
l.sort()
for i in l:
    while l.count(i) > 1:
        l.remove(i)
print(l)