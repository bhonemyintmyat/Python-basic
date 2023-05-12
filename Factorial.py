#Finding the factorial
def main():
 #input number must be greater than or equal to 0
    n=int(input("What's the number? "))
    print("Factorial is", factorial(n))

def factorial(n):
    if n<=1:
        return 1
    ans = 1
    while n>0:
        ans = ans * n
        n=n-1
    return ans

main()

