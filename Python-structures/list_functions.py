numbers = [1, 2, 3, 4, 5]
numbers.append(6)# add an element to a list at the end of the list
numbers.insert(3, 10)# add item at the specified position ie insert(index, number)
numbers.remove(10)# remove a specified element in the list here 3 !!works only if element exist
numbers.pop()# removes the last element
numbers.index(5)# returns the index of the first appearence of the specified element !!only if element exist
numbers.count(2)# returns number of occurences of specified element in the list
numbers.sort()# does not return any value only sorts the existing list ie numbers
numbers.reverse()# does not return any value only reverse the existing list
numbers.copy()# returns the exact copy of the list
numbers.clear()# truncates the list
print(2 in numbers)# 'True' if element in list 'False' if element not in the list