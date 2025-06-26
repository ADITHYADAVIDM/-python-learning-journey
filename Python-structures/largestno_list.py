l = []
n = int(input("Enter the total elements : "))
for i in range(n):
    l.append(int(input(f"Enter element {i+1} : ")))
greatest = l[0]
for i in l:
    if i > greatest:
        greatest = i
print(f"The greatest number in the list is {greatest}")