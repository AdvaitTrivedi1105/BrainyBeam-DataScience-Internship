# Q-6  Factorial, prime and odd-even from user input

def get_number():
    n = int(input("\nEnter number: "))
    return n

def factorial(num):
    ans = 1
    if (num!=0 or num!=1):
        for i in range(2,num+1):
            ans *= i
    print(f"\nFactorial: {ans}")
    return

def check_prime(num):
    # not prime if num is divisible between range 2 and half of number -> [2 and n/2]
    ans = "Yes"
    if (num > 1):
        for i in range(2,num//2):
            if (num % i == 0):
                ans = "No"
                break
    print(f"\nPrime: {ans}")
    return

def check_odd_even(num):
    if (num % 2 == 0):
        ans = "Even"
    else:
        ans = "Odd"
    print(f"\nNumber is: {ans}\n")
    return

# Main - Driver Code
num = get_number()

factorial(num)
check_prime(num)
check_odd_even(num)