weight = int(input("Enter your weight : "))
unit = input("Enter the unit (L)bs or (K)g: ")

if unit.upper() == 'K':
    print(f"Your weight is {weight/.45} pounds")
elif unit.upper() == 'L':
    print(f"Your weight is {weight*.45} kilos")
else:
    print("Enter a valid unit!!")