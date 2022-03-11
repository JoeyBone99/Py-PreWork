# Write a function to print "hello_USERNAME!" USERNAME is the input of the function. The first line of the code has been defined as below.

def hello_name(user_name):
    
    print('hello_' + user_name +'!')
    
hello_name('Joeyloke')


# Write a python function, first_odds that prints the odd numbers 
# from 1-100 and returns nothing

def first_odds():
   numbers = []
   for value in range(1,100):
      if value %2 != 0:
         numbers.append(value)
   return None
   
print(first_odds())


# Please write a Python function max_num_in_list
# to return the max number of a given list.
# The first line of the code has been defined as below.

def max_num(numbs):
   return max(numbs)
   
print(max_num([2, 4, 6, 5, 3]))


# Write a function to return if the given year is a leap year. 
# A leap year is divisible by 4, but not divisible by 100, 
# unless it is also divisible by 400. 
# The return should be boolean Type (true/false).

given_year = (2004, 2008, 2005, 2003)
def leap_year(given_year):
    for given_years in given_year:
        if given_years % 4 == 0:
            print(True)
        elif given_years % 400 == 0:
            print(True)
        elif given_years % 100 == 0:
            print(True)
        else:
            print(False)

leap_year(given_year)


# Write a function to check to see if all numbers in list are consecutive numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. The return should be boolean Type.

def consecutive(numbers):
   for i in range(len(numbers)-1):
      if numbers[i]+1 != numbers[i+1]:
        print(False)

consecutive([5, 3, 7, 13])



















    
    
