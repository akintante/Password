
def prime_checker(number):
    is_prime = True
    for i in range (2, number):
       
        if int(number) % i == 0: 
            print(i)
            is_prime = False
    if is_prime == True:
        print(f"{number} is a Prime Number")
    else:
        print(f"{number} is Not a Prime Number")
for i in range(10):
    number = int(input("Enter a number: "))
    prime_checker(number)