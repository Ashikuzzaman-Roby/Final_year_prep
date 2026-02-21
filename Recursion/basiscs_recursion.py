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




# problem 03 : 
# Sum of Nested Lists Using Recursion

# Write a Python program to sum recursion lists using recursion.

# Test Data: [1, 2, [3,4], [5,6]]
# Expected Result: 21


nested_lst = [1, 2, [3,4], [5,6]]
def nested_add(lst):
    if len(lst)==0:
        return 0
    
    if len(lst)==1:
        if type(lst[0])!=int:
            if type(lst[0])==list : 
                return nested_add(lst[0])
        else:
            return lst[0]
    else:
        if type(lst[0])!=int:
            if type(lst[0])==list : 
                return nested_add(lst[0])+nested_add(lst[1::])
            
        else:
            return lst[0]+nested_add(lst[1::])
        
print(nested_add(nested_lst))








# code forces basics :

# sheet 07 : problem solving : 

# may be it is going to be  my first accepted code 

# 01 : 
# n= int(input("please input a number : "))
n=5
def print_recursion(n): 
  if n>0 : 
    print("I love Recursion")
    print_recursion(n-1)
  return 
print_recursion(n)

# 02 : 

# n = int(input())
def print_one_n(n):
    if n>0:
        print_one_n(n-1)
        print(n)
    return 
print_one_n(n)


# 03 : 

# n = int(input())
def print_n_1(n):
    if n>0:
        if n==1:
            print(1)
        else:
            print(n,end=" ")
            print_n_1(n-1)
    return 
print_n_1(n)