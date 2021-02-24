
MAGIC_NUMBER = 8.9875517923*1e9

# Section 1
q1 = int(input('Enter a value of charge q1: '))
q2 = int(input('Enter a value of charge q2: '))
distance = int(input("Enter the distance between two charges: "))
force = MAGIC_NUMBER * q1 * q2/(distance**2)
print ("Electric Force between q1 and q2 is: ", force, "Newton")

# Section 2
num = int(input('Enter an integer number: '))
if num % 2 == 0:
    print(num, "is an even number.")
else:
    print(num, "is an odd number.")