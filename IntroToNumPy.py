import numpy as np

array = np.array([[1, 2, 3], [4, 5, 6]])

print("From this array: [1, 2, 3], [4, 5, 6]\nChoose from the following options:")
print("(1) Display the number of dimensions")
print("(2) Display the number of elements")
print("(3) Display the data type of the array")

user_input = int(input("Enter an option: "))

if user_input == 1:
    print(f"The number of dimensions are {array.ndim}.")

elif user_input == 2:
    print(f"The number of elements are {array.size}.")

elif user_input == 3:
    print(f"The data type of the array is {array.dtype}")