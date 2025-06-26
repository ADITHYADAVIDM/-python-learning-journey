name = int(input("Enter a name : "))

if len(name) < 5:
    print("Name is too short")
elif len(name) > 30:
    print("Name is too long")
else:
    print("You have a nice name!!")