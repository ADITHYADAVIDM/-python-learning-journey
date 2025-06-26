def greet_user(first_name, second_name):
    print(f"Hi there!! {first_name} {second_name}")
    print("Welcome aborad")


print("Start")# positional argument
greet_user(second_name = "bro", first_name = "david") # keyword argument
print("Finish")
# always use keyword arguments after positional arguments
# by default all functions return "None"
def square(number):
    return number * number # returns the expresion to function caller ie line 13
print(square(3))

#default parameters
def greet(name = ""):
    print(f"Hi there {name}")
greet()
greet("david")
say = greet # python functions are First class objects
say()