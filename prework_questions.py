#Question 1
# Write a function to print "hello_USERNAME!" USERNAME is the input of the function. The first line of the code has been defined as below.

#   def hello_name(user_name):
#       .....

def hello_name(user_name):
    """prints hello_USERNAME!"""
    print("hello_" + user_name.upper())

hello_name("USERNAME!\n")

#Question 2
# Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing

#   def first_odds():
#       .....

def first_odds():
    num_1 = 1
    num_2 = 100
    for num in range(num_1, num_2, 2):
        if num_1 % 2 != 0:
            return num
# To return the list of odd numbers, replace "return" with print()        
first_odds()

# Question 3
# Please write a Python function, max_num_in_list to return the max number of a given list. The first line of the code has been defined as below.

#   def max_num_in_list(a_list):
#       .....

def max_num_in_list(a_list):  
    max = a_list[0]  
    for num in a_list:  
        if num > max:  
            max = num  
    return max

print(max_num_in_list([1, 17, 25, 700, -5]))

# Question 4
# Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. The return should be boolean Type (true/false).

#   def is_leap_year(a_year):
#       .....

def is_leap_year(a_year):
    if (a_year % 4 == 0) and (a_year % 100 != 0):
        print(True)
    elif (a_year % 400 == 0):
        print(True)
    else:
        print(False)
is_leap_year(1992)

# Question 5
# Write a function to check to see if all numbers in list are consecutive numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. The return should be boolean Type.

#   def is_consecutive(a_list):
#       .....

def is_consecutive(a_list):
    return sorted(a_list) == list(range(min(a_list), max(a_list) + 1))
     
a_list = [51, 56, 52, 57, 58, 53, 55, 54, 59,]
print(is_consecutive(a_list))