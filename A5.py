# ###################################################################
# Prime numbers
# ###################################################################

# NOTE: this is a great example of a question you might be asked in a coding interview

# create a function named is_prime that returns True if the given number is prime and False otherwise
def is_prime(n):
    if n < 2:
        return False

    # you only need to check divisors up to sqrt(n)+1 
    for divisor in range(2, int(n ** 0.5) + 1):
        if n % divisor == 0:
            return False

    return True

# input an integer from the user and print if it's prime or not
number = int(input("Enter an integer: "))
if is_prime(number):
    print(f"{number} is prime.")
else:
    print(f"{number} is not prime.")

# Now, find all the prime numbers from 1 to 1000
# create an empty list to store all the prime numbers
primes = []

# loop through 1 to 1000 (range is not inclusive for the end)
for n in range(1, 1001):
    # if the number in this iteration of the loop is prime, add it to the list
    if is_prime(n):
        primes.append(n)

# print the list of prime numbers
print("Primes from 1 to 1000:")
print(primes)