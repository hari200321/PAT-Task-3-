# 1) You have been given a Python List [10,501,22,37,100,999,87,351] Your task is to Create two list one which have all the even numbers and another list which will have,
#all the odd numbers in it. 

number=[10,501,22,37,100,999,87,351]
evennumber=[ i for i in number if i%2 == 0]
oddnumber=[i for i in number if i%2 != 0]
print(evennumber,oddnumber)



# 2) Given a Python List [10,501,22,37,100,999,87,351] 
# your task is to Count all the Prime Numbers and create a new Python List which willcontain all the Prime Numbers in it?


mylist =[10,501,22,37,100,999,87,351]
prime =[]
for i in mylist:
 c=0
for j in range(1,i):
  if i%j ==0:
   c+=1
if c==1:
  prime.append(i)
print(prime)


# 3)  Given a Python List [10,501,22,37,100,999,87,351] Find out how many numbers are there in the given Python List which are Happy numbers?

a = [10,501,22,37,100,999,87,351]
b = []
def happy(a):
 for i in range (len(a)):
  sum = a[i]
while sum!=1 and sum !=4:
  tempsum = 0
for digit in str(sum):
   tempsum += int(digit) ** 2
sum = tempsum
if sum == 1:
 b.append(a[i])
print(b)
print(happy(a))


# 4) Write a python program to find the sum of the first and last digit of an integer?

number = 3456

number = str(number)

first_digit = int(number[0])

last_digit = int(number[-1])

addition = first_digit + last_digit

print("Addition of first and last digit of the number is", addition)


# 5) # You have been given a list of N integers which represents the number of Mangoes in a bag. Each bag has a variable numbers of Mangoes. There are M students in a Guvi class.
# your task is to distribute the Mangoes in such a way that each student gets one Bag. The difference between the number of Mangoes in a bag with maximum Mangoes and Bags with minimum Mangoes givento the student is minimum?

def man(n, m):
res = 1

if m > n — m:
m = n — m

for i in range(0, m):
res *= (n — i)
res /= (i + 1)

return res

# helper function for generating no of ways
# to distribute n mangoes amongst m student
def calculate(n, m):

# not enough mangoes to be distributed
if n<m:
return 0

# ways -> (m + n-1)C(m-1)
ways = man(m + n-1, m-1)
return int(ways)

# Driver function
if __name__ == ‘__main__’:

# n represents number of mangoes
# m represents number of people
n = 7 ;m = 5

result = calculate(n, m)
print(result)


# 6) You have been three lists. Your task is to find the duplicates in the three lists. 
# Write a python program for the same. You can use your own python lists?

def Intersets(arr1, arr2, arr3):
common = list(filter(lambda x: x in arr2 and x in arr3, arr1))
print(common)

arr1 = [1, 5, 10, 20, 80, 50]
arr2 = [6, 7, 20, 80, 100]
arr3 = [3, 4, 15, 20, 30, 50, 70, 80]

Intersets(arr1, arr2, arr3)


# 7) Write a Python program to find the first non-repeating elements in a given list of integers?

def count(arr, n):

visited = [False for i in range(n)]

for i in range(n):

if (visited[i] == True):
continue

count = 1
for j in range(i + 1, n, 1):
if (arr[i] == arr[j]):
visited[j] = True
count += 1
if count == 1 :
print(arr[i]);

arr = [10, 30, 40, 20, 10, 20, 50, 10]
n = len(arr)
count(arr, n)


