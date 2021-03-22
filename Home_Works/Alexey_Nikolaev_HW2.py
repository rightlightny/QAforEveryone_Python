# 1.Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.

myList = [1, 'Hello', 'my', 'World !', 3, 4]
myList = [x for (i, x) in enumerate(myList) if i not in (0, 4, 5)]
print(myList)

# 2. Write a Python program to generate and print a list except for the first 5 elements
newList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(newList[5:])

# 3. Write a Python program to assign a number to a and b and print the result of sum, subtraction, multiplication,
#      division.

a = 10
b = 3
print((a + b), (a - b), (a * b), (a // b))

# 4. Write a Python program to assign a number to either a or b and another should be a string (you can decide which
# one is string and which one is integer or assume that they can be different types every run) and print the result
# of the multiplication. Also, print changes both to string and print out “a + any word + b” 10 times where a and b
# are your values.

a = 3
b = '3'
print(a * b)
a = 'triple'
b = 3
print(a*b)
a = '3'
b = '3'
print((a + " equal to " + b)*10)


# 5. Write a Python program to print a list of integers without minimum and maximum values
myList = [-189, 1, 10, 19, 200, 200020]
myList.remove(min(myList)), myList.remove(max(myList))
print(myList)

# 6. Write a Python program to sort and then print reverse list: ['b', 'n', 'A', 'g', 'S', 'p', 'm', 'r', 'R', 'X',
# 'z', 'B', 'I', 'H', 'A', 'e', 't', 'k', 'k', 'k', 'l', 'c', 'g', 'S', 'P', 'q', 'Y', 'Q']

myList = ['b', 'n', 'A', 'g', 'S', 'p', 'm', 'r', 'R', 'X', 'z', 'B', 'I', 'H', 'A', 'e', 't', 'k', 'k', 'k', 'l', 'c',
          'g', 'S', 'P', 'q', 'Y', 'Q']
myList.sort()
myList.reverse()
print(myList)
