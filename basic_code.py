# # Even or odd number
#
# x =int(input("Enter number"))
# if x%2 == 0:
#     print("X is a even number")
# else:
#     print("X is a odd number")
#
# # max
# a = int(input("Enter first number:"))
# b = int(input("Enter second number:"))
#
# c = max(a,b)
# print("Maxnumber from tha values :",c)
# # Prime number
#
# x = int(input("Enter number"))
# if x >1:
#     for i in range(2, int(x / 2) + 1):
#         # Condition to check if the given number is divisible
#         if (x % i) == 0:
#             # If divisible by any number it's not a prime number
#             print("The number ", x, "is not a prime number")
#             break
#             # Else print it as a prime number
#     else:
#         print("The number ", x, "is a prime number")
#         # If the given number is 1
# else:
#     print("The number ", x, "is not a prime number")

# leap year
# Python program to check if year is a leap year or not

# year = 2023
# if (year % 400 == 0) and (year % 100 == 0):
#     print("{0} is a leap year".format(year))
# elif (year % 4 ==0) and (year % 100 != 0):
#     print("{0} is a leap year".format(year))
# else:
#     print("{0} is not a leap year".format(year))
# def outer_function():
#     global num
#     num = 20
#
#     def inner_function():
#         global num
#         num = 30
#         print('num =', num)
#
#     inner_function()
#     print('num =', num)
#
#
# num = 10
# outer_function()
# print('num =', num)

#Armstrong number

# number = 153
# integer_value = number
# s = 0
# while number > 0:
#     x = number % 10
#     s = s+x*x*x
#     n = number // 10
# if s == integer_value:
#     print("Armstrong number")
# else:
#     print("Not")
# my_list = ["1", "2", "3"]
# my_list.sort(key=int)
# print(my_list)

browser = input("Enter browser")
if browser == "chrome":
    print("Chrome Browser is initiated")
elif browser == "FF":
    print("Fire Fox Browser is initiated ")
elif browser == "Edge":
    print("Edge Broswer is initiated")
