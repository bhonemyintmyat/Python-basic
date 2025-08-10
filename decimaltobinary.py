def main():
    a = int(input("Decimal: "))
    
    print("Binary: ", con(a))

def con(a):
    #create an empty list to store remainders
    c = []
    #when the quotient is 0, the process finishes
    while a / 2 != 0:
        b = (a % 2)
        #not to have decimal values
        a //=2
        #store values in the list
        c.append(b)
    #reverse the list
    d = list(reversed(c))
    #concantenate the list
    result = int("".join(map(str, d)))
    return result
