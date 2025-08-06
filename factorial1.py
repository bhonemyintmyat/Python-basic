def main():
    n = int(input("Enter: "))
    print("The answer is", factorial(n))

def factorial(n):
    ans = 1
        #n = int(input("Enter: "))
        #ans = 1
    if n >= 1:
        while n > 0:
            ans = ans * n
            n = n-1
            if n == 0:
                return ans
            else:
                continue
    elif n < 0:
        return "Invalid Input"
    elif n == 0:
        return ans


if __name__ == '__main__': 
    main()
