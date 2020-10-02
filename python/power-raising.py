# a funtion pow is defined to take 2 arguments as input
def pow(x, n):
    if (n == 0):
        return 1
    else:
        return x**n


x = float(input("Enter the base no. : "))
n = int(input("Enter an integer to be raised with : "))
print(pow(x, n))
