####### Print #######

print("Aditi")
print("Sinha")
print("-----------")
print("Aditi", end=" ")
print("Sinha")

####### Input #######

lst = 0
print("Enter number of Test Cases:")
testCases = int(input())
for i in range(0, testCases):
    print(f"Test Case {i+1}")
    print("Enter value of n and k in one line delimeted by space.")
    n, k = map(int, input().split())
    print(f"n is {n} and k is {k}")
    lst = list(map(int, input().split()))
    print(f"List of {n} nos: ", lst)

print("Input Successful!")

####### Data Types | Type Conversion | Mutability #######

a = [1,2,3]
print(a, id(a))
a[1] = 6
print(a, id(a))
print("List is mutable as 'a' points to the same memory box\n")
a = [1, 6, 3]
print(a, id(a))
print("This is reassignment of new list to 'a'\n")

f = 6.6
print(f, id(f))
f = f + 1
print(f, id(f))
print("Integers and Floats are Immutable.")

s = set(a)
print(s, id(s))
s = set(a + a)
print(s, id(s))

####### LISTS #######

age = [23, 56, 89, 46, 55]
age.append(78)
print(age)
age.insert(3, 78)
print(age)
age.remove(46)
print(age)
age.pop(3)
print(age)

lst = [2, 3, 4, 5, 4, 7, 4, 8]
print(lst.count(4))

####### SETS #######

s = {4, 2, 6}
s.add(8)
print(s)
s.remove(2)
print(s)
print(8 in s)


####### DICTIONARY #######

d1 = {'a': 1, 'b': 2, 'c': 3}
d1['b'] = 5
d1['d'] = 4
del d1['c']
print(d1.items())
print(d1.keys())
print(d1.values())

l1 = [1, 2, 3]
l2 = [10, 11, 12]
d = zip(l1, l2)
print(d)

####### Find all even numbers in the array #######

lst = [1, 2, 3, 4, 5, 6]
evenList = []
for i in range(len(lst)):
    if lst[i]%2==0:
        evenList.append(i)

print(evenList)