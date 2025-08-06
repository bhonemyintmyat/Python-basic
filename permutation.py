from factorial1 import factorial

def main():
    n = int(input("n: "))
    r = int(input("r: "))
    print("nPr:", permutation(n,r))

def permutation(n,r):
    if n < r:
        return 0
    else:
        return factorial(n) / factorial(n - r)
    

if __name__ == '__main__': 
    main()
