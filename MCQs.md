{% extends "base_dealjacket.html"|tenant_template:tenant_code %}
{% load crispy_forms_tags dt_static feature_toggle %}

Python MCQs
https://www.sanfoundry.com/python-programming-interview-questions-answers/
https://pynative.com/python/quizzes/
https://www.geeksforgeeks.org/python-multiple-choice-questions/
https://realpython.com/quizzes/python-dicts/viewer/


conversion and format in detail and string function in detail spli and partition

Q1. Which of the following is correct about Python?
A. It supports automatic garbage collection.
B. It can be easily integrated with C, C++, COM, ActiveX, CORBA, and Java
C. Both of the above(Currect ans)
D. None of the above

Q.2 Which of the following statement(s) is TRUE? (A and C)
A hash function takes a message of arbitrary length and generates a fixed length code.
A hash function takes a message of fixed length and generates a code of variable length.
A hash function may give the same hash value for distinct messages.


  Hash function is defined as any function that can be used to map data of arbitrary size of data to a fixed size data.. The values returned by a hash function are called hash values, hash codes, digests, or simply hashes  :  Statement 1 is correct Yes, it is possible that a Hash Function maps a value to a same location in the memmory that's why collision occurs and we have different technique to handle  this problem : Statement 3 is coorect. eg : we have hash function, h(x) = x mod 3 Acc to Statement 1, no matter what the value of 'x' is h(x) results in a fixed mapping location. Acc. to Statement 3, h(x) can result in same mapping mapping location for different value of 'x' e.g. if x = 4 or x = 7 , h(x) = 1 in both the cases, although collision occurs. 


10. What will be the output of the following Python code?

>>> a={1,2,3}
>>> b=frozenset([3,4,5])
>>> a-b {1,2}


13. What will be the output of the following Python code?

>>> a={5,6,7,8}
>>> b={7,5,6,8}
>>> a==b
  
Q2. What does ~~~~~~5 evaluate to?
~x is equivalent to -(x+1).

Q1. What is the output of the following program :
print 0.1 + 0.2 == 0.3
Neither of 0.1, 0.2 and 0.3 can be represented accurately in binary. The round off errors from 0.1 and 0.2 accumulate and hence there is a difference of 5.5511e-17 between (0.1 + 0.2) and 0.3.

Q1.

List = [True, 50, 10]
List.insert(2, 5)   
print(sum(List))

Q.2  What is the output of the following program?
T = (2e-04, True, False, 8, 1.001, True)
val = 0
for x in T:
    val += int(x)
print(val)

Q.3 What will be the output of the following code :
print(type(type(int))) # <class 'type'>

Q5. What will be the output of the following Python code snippet?
i**-1
x = [i**+1 for i in range(3)]; print(x);
 i**+1 is evaluated as (i)**(+1).


Q 1. Looking at the below code, write down the final values of A0, A1, …An.

A0 = dict(zip(('a','b','c','d','e'),(1,2,3,4,5)))
A1 = range(10)A2 = sorted([i for i in A1 if i in A0])
A3 = sorted([A0[s] for s in A0])
A4 = [i for i in A1 if i in A3]
A5 = {i:i*i for i in A1}
A6 = [[i,i*i] for i in A1]
print(A0,A1,A2,A3,A4,A5,A6)

Q.7 What will be the output of the following Python code?

def unpack(a,b,c,d):
    print(a+d)
x = [1,2,3,4]
unpack(*x)

Q.1 What will be the output of the following Python code?

word1="Apple"
word2="Apple"
list1=[1,2,3]
list2=[1,2,3]
print(word1 is word2) True
print(list1 is list2) False


Q95. Which of the following is an invalid statement?
a) abc = 1,000,000
b) a b c = 1000 2000 3000
c) a,b,c = 1000, 2000, 3000
d) a_b_c = 1,000,000
Answer: b) a b c = 1000 2000 3000

Spaces are not allowed in variable names.


Q.1 The above copy is a type of shallow copy and only changes made in sublist is reflected in the copied list.
a=[10,23,56,[78]]
b=list(a) # b = a[:]
a[3][0]=95
a[1]=34
print(b)



Explanation: The first line of the code creates multiple reference copies of sublist. Hence when 7 is appended, it gets appended to all the sublists.

Q.8. What will be the output of the following Python code?

places = ['Bangalore', 'Mumbai', 'Delhi']
places1 = places
places2 = places[:]
places1[1]="Pune"
places2[2]="Hyderabad"
print(places)

places1 is an alias of the list places. Hence, any change made to places1 is reflected in places. places2 is a copy of the list places. Thus, any change made to places2 isn’t reflected in places.

Q.3 What will be the output of the following Python code?

lst=[3,4,6,1,2]
lst[1:2]=[7,8]
print(lst)
In the piece of code, slice assignment has been implemented. The sliced list is replaced by the assigned elements in the list.


2. What will be the output of the following Python code?

>>> a=[14,52,7]
>>>> b=a.copy() 
>>> b is a

for copy it create new object so this will be false but in case of reference b=a, this will be true.

Q.34. What is the output of the following piece of code?

print([45]*4) 
print((45)*4)
print((45,)*4)


Q.2 What will be the output of the following Python code?(reference)

a=[[]]*3
a[1].append(7)
print(a)



Q.0. What will be the output of the following Python code?

def f(i, values = []):
    values.append(i)
    return values
 
f(1)
f(2)
v = f(3)
print(v)
a) [1] [2] [3]
b) [1] [1, 2] [1, 2, 3]
c) [1, 2, 3]
d) 1 2 3

1. The function sqrt() from the math module computes the square root of a number.
Will the highlighted line of code raise an exception?

x = -100
from math import sqrt
x > 0 and sqrt(x)


2. 
t = *(x for x in range(10)), # tuple (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
print (t)
print(type(t))

3. What is the output of the following list assignment

aList = [4, 8, 12, 16]
aList[1:4] = [20, 24, 28]
print(aList)


4. What is the output of the following list comprehension

resList = [x+y for x in ['Hello ', 'Good '] for y in ['Dear', 'Bye']]
print(resList)
 [‘Hello Dear’, ‘Hello Bye’, ‘Good Dear’, ‘Good Bye’]
 [‘Hello Dear’, ‘Good Dear’, ‘Hello Bye’, ‘Good Bye’]
 

5. What is the output of the following code?

sampleList = [10, 20, 30, 40]
del sampleList[0:6]
print(sampleList)
 []
 list index out of range.
 [10, 20]
 
6. What will be the output of the following Python code?
def change(val,l=[]):
    print(l)
    l.append(val)
    return l

change(4)
change(5)
m = change(6)
print(m)
	
	
7. What will be the output of the following Python code?

names1 = ['Amir', 'Bear', 'Charlton', 'Daman']
names2 = names1
names3 = names1[:]
 
names2[0] = 'Alice'
names3[1] = 'Bob'
 
sum = 0
for ls in (names1, names2, names3):
    if ls[0] == 'Alice':
        sum += 1
    if ls[1] == 'Bob':
        sum += 10
 
print sum

8. What will be the output of the following Python code?

>>>list1 = [1, 3]
>>>list2 = list1
>>>list1[0] = 4
>>>print(list2)
Explanation: Lists should be copied by executing [:] operation.

9. What will be the output of the following Python code?

>>>list1 = [11, 2, 23]
>>>list2 = [11, 2, 2]
>>>list1 < list2 is


10. What will be the output of the following Python code?(call by value)

def f(values):
    values[0] = 44
 
v = [1, 2, 3]
f(v)
print(v)



Predict the output of below programs.

Q1. 
a = True
b = False
c = False
if a or b and c:
    print("if statement")
else:
    print("else statement")

Output: if statement


Q2. Please correct the code syntax and give us the output of the code
try:
    a = 10 / 0
except:
    print("except")
except ZeroDivisionError as e:
    print('ZeroDivisionError')
finally:
    print("finally")
else:
    print("else")


try:
    a = 10 / 0
except ZeroDivisionError as e:
    print('ZeroDivisionError')
except:
    print("except")
else:
    print("else")
finally:
    print("finally")


Currect code:
try:
    a = 10 / 0
except ZeroDivisionError as e:
    print('ZeroDivisionError')
except:
    print("except")
else:
    print("else")
finally:
    print("finally")

Output: ZeroDivisionError
        finally

Q3. 	
d = {'a':'a', 1:1, 3.4:3.4, [1,2,3]:[1,2,3], (1,2,3):(1,2,3),}
print(d[(1,2,3)])
print(d[[1,2,3]])

output: TypeError: unhashable type: 'list'

Q4. 
l = [1,'hi', 'dog','kapil jain', 3.4]
l.sort() 

output: TypeError: '<' not supported between instances of 'str' and 'int'

Q5. 
def gfg(x,l=[]): 
	for i in range(x): 
		l.append(i*i) 
	print(l) 

gfg(2) # [0, 1]
gfg(3,[3,2,1]) # [3, 2, 1, 0, 1, 4]
gfg(3) # [0, 1, 0, 1, 4]


Q6. 
d = {}
d[1]=1
print(d)

l = []
l[0]=0
print(l) # IndexError: list assignment index out of range


Q7. 
def test(*args, **kwargs):
    print (type(args), type(kwargs))

test(1,2,x=3) 
test(x=3,4)  this 
test(1,2,x=3,4) 



def printinfo1( age = 35, fame, lname ):
    "This prints a passed info into this function"
    print ("Name: ", fname)
    print ("Age ", age)
    return

# Now you can call printinfo_ function
printinfo1( age = 50, name = "m",”j” )

output:
# <class 'tuple'> <class 'dict'>
# SyntaxError: positional argument follows keyword argument
# SyntaxError: positional argument follows keyword argument


Q8. Does python support method overloading?
class Test:
	def product(self, a, b): 
		return a * b
      
	def product(self, a, b, c): 
		return a * b * c 

Obj = Test()
print(Obj.product(3,5))
print(Obj.product(1,3,5)) 

output:
TypeError: product() missing 1 required positional argument: 'c'
15
 


Python Programs:
Q1. write a program to replace all the vovels from a string with * using list comprehension.
print(''.join([ch if ch not in 'aeiou' else '*' for ch in 'kapiljain']))

Q2. Check if the given string is complete or not
{([({{}})])} # True
{([({{}}])}  # False

Q3. How do you remove duplicates from a list?
	mylist = [1,2,3,4,5,7,2,5,6,2,4,6,8,53,5,35,6,3,5,5,5,5]

	# Method 1: without using any other list
	if mylist:
		mylist.sort()
		last = mylist[-1]
		for i in range(len(mylist)-2, -1, -1):
			if last == mylist[i]:
				del mylist[i]
			else:
				last = mylist[i]
	print(mylist)
				

	# Method 2: without using any other list     
	if mylist:
		mylist.sort()
		first = mylist[0]
		i = 1
		while(i < len(mylist)):
			if first == mylist[i]:
				del mylist[i]
			else:
				first = mylist[i]
				i += 1
	print(mylist)


	# Method 3:
	if mylist:
		output_list = []
		for i in mylist:
			if i not in output_list:
				output_list.append(i)
	print(output_list)


	# Method 4:
	print(list(set(mylist)))

If all elements of the list may be used as set keys (i.e. they are all hashable) this is often faster
mylist = list(set(mylist))
This converts the list into a set, thereby removing duplicates, and then back into a list.




http://net-informations.com/python/default.htm
Python Interview Questions:*


5. What is mutable and immutable objects?
50. Why dictionary keys must be immutable?
35. How to retrive data from a table in postgresql database through python?
36. What is GIL Lock?

44. What is the different between old class style and new class style?

48. What is tuple unpacking?
49. Name some of the python error tht you know?


56. What's wrong with import all?
57. Meaning of single and double underscore before an object name?
58. How to call an shell external command in python?
60. Why python is not fully object oriented language?

What is threading limitation in python?
How to modify the string in python?
What is run time and compile time in python?
How to implement Enum in python?
How to kill a thread in python? (# http://net-informations.com/python/default.htm)
