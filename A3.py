def numberofbits(n):
    count = 0
    while(n):
        count += 1
        n >>= 1
    return count

number = int(input("Enter your number: "))
print("Total bits: " + str(numberofbits(number)))
