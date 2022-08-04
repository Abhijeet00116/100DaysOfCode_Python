def factorial(i):
    if i<=1:
        return i
    else:
        return (i * factorial(i-1))

if __name__=='__main__':
    num = int(input("ENTER A POSITIVE INTEGER -: "))
    if num>=0:
        print("Factorial of ",num," is -: ",factorial(num))
    else:
        print("Pls Enter a +ve integer...")