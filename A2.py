def isevenorodd(n):
    if (n ^ 1) == n + 1:
        return True
    else:
        return False

number = int(input("Enter a number: "))
if isevenorodd(number):
    print("even")
else:
    print("odd")

