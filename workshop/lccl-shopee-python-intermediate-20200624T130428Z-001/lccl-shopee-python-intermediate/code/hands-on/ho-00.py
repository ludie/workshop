# by LCCL Coding Academy, www.LccLcoding.com
# for Shopee Code League 2020

print()

# List of prime numbers 

def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return None
    return n >= 2

primes = [x for x in range(2, 100) if is_prime(x)]

print('Prime numbers between 0 and 100: ')
print(primes)


# Sum of prime numbers

print('\nSum:')
print(sum(primes))


# Digit sums

def digit_sum(n):
    while n > 9:
        n = sum([int(i) for i in str(n)])
    return n

print('\nDigit Sums:')
print(list(map(digit_sum, primes)))

# String all numbers
print('\nString of primes:')
print(''.join(str(n) for n in primes))

print()


