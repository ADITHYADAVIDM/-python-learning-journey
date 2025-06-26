i = 1
while i <= 5:
    print(i)
    i += 1
print("Done")

i = 1
while i <= 5:
    print("*" * i)
    i += 1
print("Done")

a = int(input("Enter a number (secretly) : "))
d = input("Enter Difficulty [E]asy, [M]edium, [Hard] : ")
if d.upper() == 'E':
    diff = 6
elif d.upper() == "M":
    diff = 4
elif d.upper() == "H":
    diff = 2
else:
    print("Enter a valid difficulty!!")
print("Start guessing the number your friend entered")
i = len(str(a))
j = 1
while i > 1:
    j *= 10 
    i -= 1
j *= diff
flag = 0
while j > 0:
    j -= 1
    b = int(input("GUESS : "))
    if a == b:
        flag = 1
        break
if flag == 0:
    print("Sorry you are out of chance!!")
else:
    print("WOW!! you guessed right!!")