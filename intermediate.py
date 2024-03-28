########################## Count digits in a number

######## Approach 1
n = int(input())
# c = len(str(n))
# print(c)

######## Approach 2
import math
c = math.floor(math.log10(n)) + 1
c1 = math.ceil(math.log10(n))
print(c, c1)

########################## Reverse a number

n = int(input())
rev = 0
while n:
    d = n%10
    rev = rev * 10 + d
    n = n//10
print(rev)

########################## Palindrome

n = int(input())
rev = 0
n1 = n
while n1:
    d = n1%10
    rev = rev*10 + d
    n1 = n1//10
if rev == n:
    print(f"{n} is a Palindrome.")
else:
    print(f"{n} is not a Palindrome.")

########################## GCD or HCF of a number

a, b = map(int, input().split())
print(f"HCF or GCD of {a} and {b} is ")
n1 = max(a, b)
n = min(a,b)
while n:
    r = n1%n
    n1 = n
    n = r

print(n1)

########################## Armstrong

import sys
sys.set_int_max_str_digits(0)  # To avoid limit exceeded error during integer to string conversion using len()

n = int(input())
c = len(str(n))
n1 = n
arm = 0
while n1:
    d = n1%10
    arm = arm + (d**c)
    n1 = n1//10

if arm == n:
    print("ArmStrong.")

########################## Print all Divisors

# n = int(input())


########################## Check for prime

n = int(input())
f=0
for i in range(2, n):
    if n%i == 0:
        f=1
        break
if f==0:
    print(f"{n} is prime.")

####### Optimized Approach - run uptil sq. root of n

n = int(input())
i = 2
f = 0
while (i*i)==n:
    if n%i == 0:
        f = 1
        break
    i+=1
if f==0:
    print(f"{n} is prime.")

########################## Factorial of a number

n = int(input())
fact = 1
for i in range(2, n+1):
    fact = fact * i

print(f"Factorial of {n} is {fact}.")

########################## Print a Name n times

def namePrinter(n):
    if n==0:
        return
    print(f"{n} Aditi Sinha")
    namePrinter(n-1)

n = int(input())
namePrinter(n)

########################## Print 1 to n using recusrion

def iterate(i, n):
    if n==0:
        return
    print(f"Iteration {i}")
    iterate(i+1, n-1)

n = int(input())
iterate(1, n)

########################## Print n to 1 using recursion

def iterate(n):
    if n==0:
        return
    print(f"Iteration {n}")
    iterate(n-1)

n = int(input())
iterate(n)

########################## sum of first n numbers

def sumOfN(total, n):
    if n==0:
        return total
    total = total + n
    sumOfN(total, n-1)

n = int(input())
total = 0
x = sumOfN(total, n)
print(x)

########################## Fibonacci Number

def fibonnaci(a, b, n):
    if n==0:
        return b
    total = a + b
    fibonnaci(b, total, n-1)

a, b, n = map(int, input().split())
total = 0
total = fibonnaci(a, b, n)
if total == n:
    print(f"{n} is a Fibonacci number.")

########################## Count frequency of elements in array

def frequency(arr):
    d = {}
    for i in range(len(arr)):
        if arr[i] not in d:
            d[arr[i]]=1
        else:
            d[arr[i]]+=1
    return d

arr = list(map(int, input().split()))
d = frequency(arr)
print(d.items())

########################## Element of Max. and Min Frequency in array

maxElements = []
minElements = []
for k, v in d.items():
    if v == max(d.values()):
        maxElements.append(k)
    if v == min(d.values()):
        minElements.append(k)
print(maxElements, minElements)

########################## Linear search using Recursion



##########################

##########################

##########################

##########################

##########################

##########################
