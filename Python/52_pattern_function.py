# n=3
# for i in range(3):
#     print("*"*(n-i))

def pattern(n):
    for i in range(n):
        print("*"*(n-i))

n=int(input("Enter the value of n to print pattern\n"))
pattern(n)