try:
    age = int(input("Enter an age : "))
    print(age)
    income = 20000
    risk = income/age
except ValueError:
    print("Invalid value")
except ZeroDivisionError:
    print("Age cannot be zero")
finally:# executes all the code written inside the block regardless of the exception
    print("Any files that has to be closeed or any cleanup")