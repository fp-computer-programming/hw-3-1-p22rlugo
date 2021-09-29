# Ryan Lugo: RJL 9/29/21

given_number = int(input("What's your given number?: "))
muliple_number = int(input("Which multiple number do you want to divide the given by? (2, 3, , 5): "))
divisible = given_number / muliple_number

if divisible % 1 == 0:
    print("This number is divisible.")
else:
    print(given_number,"is not divisible by",muliple_number)