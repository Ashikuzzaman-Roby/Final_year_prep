print("Hello world")


def number_conversion(n,b):
    if n<b:
        return n 
    return str(number_conversion(n//b,b))+str(number_conversion(n%b,b))
x=number_conversion(18,2)
print(x)
