# solving 11 problem from w3 resources  

# problem 01 : 
# Sum of List Using Recursion

# Write a Python program to calculate the sum of a list of numbers using recursion.


# problem 01 : 
lst = [7,3,8,4,2]
def list_add(lst):
    if len(lst)==1 : 
        return lst[0]
    return lst[0]+list_add(lst[1::])
print(list_add(lst))








# problem statement 02 : 
def number_conversion(n,b):
    string = "0123456789ABCDEF"

    if n<b:
        return string[n]
    return number_conversion(n//b,b)+string[n%b]
x=number_conversion(18,2)
print(x)
