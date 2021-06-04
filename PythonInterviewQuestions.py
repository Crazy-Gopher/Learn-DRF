https://www.interviewbit.com/python-interview-questions/

Q.1 What is the difference between python 2 and 3? MRO, Exception handling, input, as, class, range, generator object
	Table below explains the difference between Python version 2 and Python version 3.

	S.No	Section	Python Version2	Python Version3
	1.	Print Function	
	Print command can be used without parentheses.

	Python 3 needs parentheses to print any string. It will raise error without parentheses.

	2.	Unicode	
	ASCII str() types and separate Unicode() but there is no byte type code in Python 2.

	Unicode (utf-8) and it has two byte classes -

	Byte
	Bytearray S.
	3.	Exceptions	
	Python 2 accepts both new and old notations of syntax.

	Python 3 raises a SyntaxError in turn when we don’t enclose the exception argument in parentheses.

	4.	Comparing Unorderable	
	It does not raise any error.

	It raises ‘TypeError’ as warning if we try to compare unorderable types.


Q.2 How to comment multiple lines in python?
	Ans: Multi-line comments appear in more than one line. All the lines to be commented are to be prefixed by a #. You can also a very good shortcut method to comment multiple lines. All you need to do is hold the ctrl key and left click in every place wherever you want to include a # character and type a # just once. This will comment all the lines where you introduced your cursor.

Q.3 What is docstring in Python? What is the difference between docstring and comment?
	A Python documentation string is known as docstring, it is a way of documenting Python functions, modules and classes.
	Docstrings are not actually comments, but, they are documentation strings. These docstrings are within triple quotes. They are not assigned to any variable and therefore, at times, serve the purpose of comments as well.
	To get a function’s docstring, we use its __doc__ attribute.

	Comments in Python start with a # character. However, alternatively at times, commenting is done using docstrings(strings enclosed within triple quotes).
	Example:
	#Comments in Python start like this
	print("Comments in Python start with a #")
	Output:  Comments in Python start with a #


Q.4 How can you copy an object in Python? What is the difference between shallow copy and deep copy?
	To copy an object in Python, you can try copy.copy () or copy.deepcopy() for the general case. You cannot copy all objects but most of them.

	Shallow copy is used when a new instance type gets created and it keeps the values that are copied in the new instance. Shallow copy is used to copy the reference pointers just like it copies the values. These references point to the original objects and the changes made in any member of the class will also affect the original copy of it. Shallow copy allows faster execution of the program and it depends on the size of the data that is used.

	Deep copy is used to store the values that are already copied. Deep copy doesn’t copy the reference pointers to the objects. It makes the reference to an object and the new object that is pointed by some other object gets stored. The changes made in the original copy won’t affect any other copy that uses the object. Deep copy makes execution of the program slower due to making certain copies for each object that is been called.

	This creates problems for only mutable object like list dictionary, set
	Shallow copy take care of object at object level but Deep copy take care of reference of references
	shallow copy is faster because it does copy the whole structure of each references
	"""
	l1 = [1,2,3,4,5]
	l2 = l1 # reference variable
	l1.append(6)
	print(l1) #[1, 2, 3, 4, 5, 6]
	print(l2) #[1, 2, 3, 4, 5, 6]

	l = [1,2,[3,4]]
	import copy
	l1 = copy.copy(l) # shallow copy
	l2 = copy.deepcopy(l) # deepcopy

	l[2][1] = 'Kapil'
	print(l) # [1, 2, [3, 'Kapil']]
	print(l1) #[1, 2, [3, 'Kapil']]
	print(l2) #[1, 2, [3, 4]]
	
	
Q.5 What is the difference between range and xrange?
	For the most part, xrange and range are the exact same in terms of functionality. They both provide a way to generate a list of integers for you to use, however you please. The only difference is that range returns a Python list object and x range returns an xrange object.
	This means that xrange doesn’t actually generate a static list at run-time like range does. It creates the values as you need them with a special technique called yielding. This technique is used with a type of object known as generators. That means that if you have a really gigantic range you’d like to generate a list for, say one billion, xrange is the function to use.
	This is especially true if you have a really memory sensitive system such as a cell phone that you are working with, as range will use as much memory as it can to create your array of integers, which can result in a Memory Error and crash your program. It’s a memory hungry beast.

	Note: xrange has been deprecated as of Python 3.x. Now range does exactly the same what xrange used to do in Python 2.x, since it was way better to use xrange() than the original range() function in Python 2.x.

Q.6 What is the difference between list and tuple?
	1. Syntax Differences: Syntax of list and tuple is slightly different. Lists are surrounded by square brackets [] and Tuples are surrounded by parenthesis ().
	2. Mutable List vs Immutable Tuples: List has mutable nature i.e., list can be changed or modified after its creation according to needs whereas tuple has immutable nature i.e., tuple can’t be changed or modified after its creation.
	3. Size Comparison: Tuples operation has smaller size than that of list, which makes it a bit faster but not that much to mention about until you have a huge number of elements.
	import sys
	  
	c=sys.getsizeof(('g','e','e','k','s'))
	print(c) # 40
	   
	d=sys.getsizeof(['g','e','e','k','s'])
	print(d) # 48
	   
	e=sys.getsizeof({'g','e','e','k','s'})
	print(e) # 108
	

Q.7 What is the difference between staticmethod, classmethod and instance method?
	1. A Instance Method: A method defind inside the class is called instance method. A instance method takes self as first parameter.

	2. A class method receives the class as implicit first argument, just like an instance method receives the instance
		1. A class method is a method which is bound to the class and not the object of the class.
		2. They have the access to the state of the class as it takes a class parameter that points to the class and not the object instance.
		3. It can modify a class state that would apply across all the instances of the class. For example it can modify a class variable that will be applicable to all the instances.
		
	3. A staticmethod is a method that knows nothing about the class or instance it was called on. It just gets the arguments that were passed, no implicit first argument. A staticmethod isn't useless - it's a way of putting a function into a class (because it logically belongs there), while indicating that it does not require access to the class
		1. A static method is also a method which is bound to the class and not the object of the class.
		2. A static method can't access or modify class state.
		3. It is present in a class because it makes sense for the method to be present in class.
		
	Class method vs Static Method
		A class method takes cls as first parameter while a static method needs no specific parameters.
		A class method can access or modify class state while a static method can't access or modify it.
		We use @classmethod decorator in python to create a class method and we use @staticmethod decorator to create a static method in python.

	Note: self and cls are madatory name, you can pass any name like clss, and selfee
	
	from datetime import date
	class Person:
		def __init__(selfee, name, age):
			selfee.name = name
			selfee.age = age
		 
		# a class method to create a Person object by birth year.
		@classmethod
		def fromBirthYear(clss, name, year):
			return clss(name, date.today().year - year)
		 
		# a static method to check if a Person is adult or not.
		@staticmethod
		def isAdult(age):
			return age > 18
	 
	person1 = Person('mayank', 21)
	person2 = Person.fromBirthYear('mayank', 2000)
	print (person1.age)#21
	print (person2.age)#21
	# print the result
	print (Person.isAdult(22))#True


Q.8 What is the difference between list comprehension and generator expression?
	difference between a list comprehension and a generator expression:
	1. The major difference between a list comprehension and a generator expression is that while list comprehension produces the entire list, generator expression produces one item at a time.
	They are kind of lazy, producing items only when asked for. For this reason, a generator expression is much more memory efficient than an equivalent list comprehension.
	2. Memory Efficient
	A normal functionEx to return a sequence will create the entire sequence in memory before returning the result. This is an overkill if the number of items in the sequence is very large. Generator implementation of such sequence is memory friendly and is preferred since it only produces one item at a time.


Q.9 What is the difference between .py and .pyc files?

Q.10 What is the difference between raw_input and input method?

Q.11 What is the difference between Python Arrays and lists?
	Ans: Arrays and lists, in Python, have the same way of storing data. But, arrays can hold only a single data type elements whereas lists can hold any data type elements.

	import array as arr
	My_Array=arr.array('i',[1,2,3,4])
	My_list=[1,'abc',1.20]
	print(My_Array)
	print(My_list)
	Output:
	array(‘i’, [1, 2, 3, 4]) [1, ‘abc’, 1.2]

Q.12 Explain the difference between local and global namespaces?
	Ans: Local namespaces are created within a function when that function is called. Global namespaces are created when the program starts.

Q.13 What is the difference between == and is operator?
	The is operator compares the identity of two objects while the == operator compares the values of two objects.
	The == operator is used when the values of two operands are equal, then the condition becomes true.
	The is operator evaluates to true if the variables on either side of the operator point to the same object and false otherwise.

Q.14 What is the difference between '__str__' and '__repr__' method?

Q.15 What is the difference between 'str' and 'repr' method?

Q.16 What is the difference between '__init__' and '__new__' method?


## OOPs

Q48. Does Python have OOps concepts?
	Ans: Python is an object-oriented programming language. This means that any program can be solved in python by creating an object model. However, Python can be treated as procedural as well as structural language

Q64. What does an object() do?
	Ans: It returns a featureless object that is a base for all classes. Also, it does not take any parameters.
	

Q61. How do you do data abstraction in Python?
	Ans: Data Abstraction is providing only the required details and hiding the implementation from the world. It can be achieved in Python by using interfaces and abstract classes.
	

Q55. Explain Inheritance in Python with an example.
	Ans: Inheritance allows One class to gain all the members(say attributes and methods) of another class. Inheritance provides code reusability, makes it easier to create and maintain an application. The class from which we are inheriting is called super-class and the class that is inherited is called a derived / child class.

	They are different types of inheritance supported by Python:

	Single Inheritance – where a derived class acquires the members of a single super class.
	Multi-level inheritance – a derived class d1 in inherited from base class base1, and d2 are inherited from base2.
	Hierarchical inheritance – from one base class you can inherit any number of child classes
	Multiple inheritance – a derived class is inherited from more than one base class.


Q59. What is Polymorphism in Python?
	Ans: Polymorphism means the ability to take multiple forms. So, for instance, if the parent class has a method named ABC then the child class also can have a method with the same name ABC having its own parameters and variables. Python allows polymorphism.


Q60. Define encapsulation in Python?
	Ans: Encapsulation means binding the code and the data together. A Python class in an example of encapsulation.


Q62.Does python make use of access specifiers?
	Ans: Python does not deprive access to an instance variable or function. Python lays down the concept of prefixing the name of the variable, function or method with a single or double underscore to imitate the behavior of protected and private access specifiers.
	
	Global variables are public variables that are defined in the global scope. To use the variable in the global scope inside a function, we use the global keyword.
	Protected attributes are attributes defined with a underscore prefixed to their identifier eg. _sara. They can still be accessed and modified from outside the class they are defined in but a responsible developer should refrain from doing so.
	Private attributes are attributes with double underscore prefixed to their identifier eg. __ansh. They cannot be accessed or modified from the outside directly and will result in an AttributeError if such an attempt is made.

Q30. How do I create static class data and static class methods?
	Both static data and static methods (in the sense of C++ or Java) are supported in Python.
	For static data, simply define a class attribute. To assign a new value to the attribute, you have to explicitly use the class name in the assignment:
	Static method can be created using staticmethod decorator.

	class C:
		@staticmethod
		def static(arg1, arg2, arg3):


Q22. Does python support method overloading?
	No, if you create two method with same name and difference signature, interpitter will override the first method with second.
	

Q15. What is MRO?
	Method Resolution Order (MRO) : It's the order in which method should be inherited in the presence of multiple inheritance. You can view the MRO by using __mro__ attribute.
	print(Fourth.__mro__) or print(help(Fourth))
	(
	<class '__main__.Fourth'>, 
	<class '__main__.Third'>, 
	<class '__main__.Second'>, 
	<class '__main__.First'>, 
	<class '__main__.Zeroth'>, 
	<class '__main__.Number'>, 
	<class 'object'>
	)
	Here is how MRO is calculated in Python:  
		1. A method in the derived calls is always called before the method of the base class. 
		2. the class which is appear first, method will get called for that class only in case of same method.
		3. In case of multiple inheritance, If both the parents have the same grand parent , then it cover all sibling first then go to grand parent class.
		4. In case of multiple inheritance, If both the parents have the different grand parent ,then it call whichever class appear first and complate its familiy(up to top level parent) then go to next class and so on.
		5. In case of multiple inheritance and super, first parent should write super().__init__() or super().sub_method() to call the second parent __init__ or sub_method. if first parent will not write then it will never called second parent.


Q14. What is multiple inheritance and explain diamond problem?
	   Zeroth(Super Base class)
	   /    \
	First Second(Base classes)
	   \    /
	   Third(child class)

	class Zeroth(object):
		def add(self):
			print("Zeroth")

	class First(Zeroth):
		def add(self):
			print("First")

	class Second(Zeroth):
		def add(self):
			print("second")

	class Third(First,Second):
		def __init__(self):
			pass
	o = Third()
	o.add()

	output: First


Q11. What is class variable and instance variable?
	Class Variables : Class variables are defined within the class construction. Because they are owned by the class itself, class variables are shared by all instances of the class. They therefore will generally have the same value for every instance unless you are using the class variable to initialize a variable.
	Instance Variables : Instance variables are owned by instances of the class. This means that for each object or instance of a class, the instance variables are different. 
	class Shark:
		animal_type = "fish" # class variable

		def __init__(self, name, age):
			self.name = name # instance variable
			self.age = age


Q9. What does self and super keyword do?
	The self is a Python keyword which represents a variable that holds the instance of an object.
	The super() builtin returns a proxy object that allows you to refer parent class by 'super'.
	Python 2: super(SubClass, self).__init__()
	Python 3: super().__init__()
	In Python, super() built-in has two major use cases:
	1. Allows us to avoid using base class explicitly
	2. Working with Multiple Inheritance

	Self is an instance or an object of a class. In Python, this is explicitly included as the first parameter. However, this is not the case in Java where it’s optional.  It helps to differentiate between the methods and attributes of a class with local variables.
	The self variable in the init method refers to the newly created object while in other methods, it refers to the object whose method was called.
	
	
Q. What is __init__?
	__init__ is a method or constructor in Python. This method is automatically called to allocate memory when a new object/ instance of a class is created. All classes have the __init__ method.

	class Employee:
	def __init__(self, name, age,salary):
	self.name = name
	self.age = age
	self.salary = 20000
	E1 = Employee("XYZ", 23, 20000)
	# E1 is the instance of class Employee.
	#__init__ allocates memory for E1. 
	print(E1.name)
	print(E1.age)
	print(E1.salary)


## Syntax


## Threading

Q.30. Can you explain the life cycle of a thread?
	To create a thread, we create a class that we make override the run method of the thread class. Then, we instantiate it.
	A thread that we just created is in the new state. When we make a call to start() on it, it forwards the threads for scheduling. These are in the ready state.
	When execution begins, the thread is in the running state.
	Calls to methods like sleep() and join() make a thread wait. Such a thread is in the waiting/blocked state.
	When a thread is done waiting or executing, other waiting threads are sent for scheduling.
	A running thread that is done executing terminates and is in the dead state.
	

Q27. What is thread synchronization, how you can achieve this in python?
	Thread synchronization is defined as a mechanism which ensures that two or more concurrent threads do not simultaneously execute some program segment known as critical section.
	Critical section refers to the parts of the program where the shared resource is accessed. Concurrent accesses to shared resource can lead to race condition.
	threading module provides a Lock class to deal with the race conditions. Lock is implemented using a Semaphore object provided by the Operating System.
	Lock class provides following methods:
		acquire([blocking]) : To acquire a lock. 
		release() : To release a lock. 
	In the critical section of target function, we apply lock using lock.acquire() method. As soon as a lock is acquired, no other thread can access the critical section (here, increment function) until the lock is released using lock.release() method.


Q19. How is Multithreading achieved in Python?
	1. Python has a multi-threading package but if you want to multi-thread to speed your code up, then it’s usually not a good idea to use it.
	2. Python has a construct called the Global Interpreter Lock (GIL). The GIL makes sure that only one of your ‘threads’ can execute at any one time. A thread acquires the GIL, does a little work, then passes the GIL onto the next thread.
	3. This happens very quickly so to the human eye it may seem like your threads are executing in parallel, but they are really just taking turns using the same CPU core.
	4. All this GIL passing adds overhead to execution. This means that if you want to make your code run faster then using the threading package often isn’t a good idea.
	
Q. what is threading limitation of python?


## Package, module

Q54. How to import modules in python?
	Modules can be imported using the import keyword.  You can import modules in three ways-
	import array           #importing using the original module name
	import array as arr    # importing using an alias name
	from array import *    #imports everything present in the array module

Q. Can we write the code inside __init__.py file?
	It is used to import a module in a directory, which is called package import.

	If we have a module, dir1/dir2/mod.py, we put __init__.py in each directories so that we can import the mod like this:

	import dir1.dir2.mod
	The __init__.py is usually an empty py file. The hierarchy gives us a convenient way of organizing the files in a large system.
	

8. What is Scope in Python?
	Every object in Python functions within a scope. A scope is a block of code where an object in Python remains relevant. Namespaces uniquely identify all the objects inside a program. However, these namespaces also have a scope defined for them where you could use their objects without any prefix. A few examples of scope created during code execution in Python are as follows:

	A local scope refers to the local objects available in the current function.
	A global scope refers to the objects available throught the code execution since their inception.
	A module-level scope refers to the global objects of the current module accessible in the program.
	An outermost scope refers to all the built-in names callable in the program. The objects in this scope are searched last to find the name referenced.
	Note: Local scope objects can be synced with global scope objects using keywords such as global.
	

Q31. What is __init__.py file and what is the use of it?
	The __init__.py file makes Python treat directories containing it as modules. Furthermore, this is the first file to be loaded in a module, so you can use it 
	to execute code that you want to run each time a module is loaded, or specify the submodules to be exported.


Q1. What are Python namespaces? Why are they used?
	A namespace in Python ensures that object names in a program are unique and can be used without any conflict. Python implements these namespaces as dictionaries with 'name as key' mapped to a corresponding 'object as value'. This allows for multiple namespaces to use the same name and map it to a separate object. A few examples of namespaces are as follows:

	Local Namespace includes local names inside a function. the namespace is temporarily created for a function call and gets cleared when the function returns.
	Global Namespace includes names from various imported packages/ modules that is being used in the current project. This namespace is created when the package is imported in the script and lasts until the execution of the script.
	Built-in Namespace includes built-in functions of core Python and built-in names for various types of exceptions.
	Lifecycle of a namespace depends upon the scope of objects they are mapped to. If the scope of an object ends, the lifecycle of that namespace comes to an end. Hence, it isn't possible to access inner namespace objects from an outer namespace.
	

47Q. How can we access a module written in Python from C?
	Python Certification Training!
	Explore Curriculum
	Ans: We can access the module written in Python from C by using the following method.

	1
	Module == PyImport_ImportModule("<modulename>");
	

Q. What do you understand by the term namespace in Python?
	Ans: A namespace in Python can be defined as a system that is designed to provide a unique name for every object in python. Types of namespaces that are present in Python are:

	Local namespace
	Global namespace
	Built-in namespace
	Scope of an object in Python: 

	Scope refers to the availability and accessibility of an object in the coding region.


Q-83: What Is The Use Of Globals() Function In Python?
	The globals() function in Python returns the current global symbol table as a dictionary object.

	Python maintains a symbol table to keep all necessary information about a program. This info includes the names of variables, methods, and classes used by the program.

	All the information in this table remains in the global scope of the program and Python allows us to retrieve it using the globals() method.

	Signature: globals()

	Arguments: None
	# Example: globals() function 
	x = 9
	def fn(): 
		y = 3
		z = y + x
		# Calling the globals() method
		z = globals()['x'] = z
		return z
		   
	# Test Code     
	ret = fn() 
	print(ret)
	The output is:

	12


Q.28 What are local, non-local and global variables in Python?
	Variables declared outside a function or in global space are called global variables. These variables can be accessed by any function in the program.
	Local Variables: Any variable declared inside a function is known as a local variable. This variable is present in the local space and not in the global space.

	Example:
	a=2
	def add():
		b=3
		c=a+b
		print(c)
	add()
	Output: 5
	When you try to access the local variable outside the function add(), it will throw an error.

	a = 15
	def outer_function():
		global a
		a = 5
		def inner_function():
			#nonlocal a # if you don't declare as nonlocal output will be 10, 5 but if you declare as nonlocal output will be 10, 10
			
			a = 10
			print("Inner functionEx: ",a)
		inner_function()
		print("Outer functionEx: ",a)
	outer_function()
	
Q28. How do I share global variables across modules?
	The canonical way to share information across modules within a single program is to create a special module (often called config or cfg). Just import the config module in all modules of your application; the module then becomes available as a global name. Because there is only one instance of each module, any changes made to the module object get reflected everywhere. For example:

	config.py:
	x = 0   # Default value of the 'x' configuration setting

	mod.py:
	import config
	config.x = 1

	main.py:
	import config
	import mod
	print(config.x)
	
	
Q. What is the namespace in python? explain local and global namespace?
	In Python, every name introduced has a place where it lives and can be hooked for. This is known as namespace. It is like a box where a variable name is mapped to the object placed. Whenever the variable is searched out, this box will be searched, to get corresponding object.


Q. What is module and packages in python? What are python modules? Name some commonly used built-in modules in Python?
	1. Modules in Python are simply Python files with a .py extension. The name of the module will be the name of the file. A Python module can have a set of functions, classes or variables defined and implemented.
	2. Packages are namespaces which contain multiple packages and modules themselves. They are simply directories, but with a twist.
	Each package in Python is a directory which MUST contain a special file called __init__.py. This file can be empty, and it indicates that the directory it contains is a Python package, so it can be imported the same way a module can be imported.

	Python modules are files containing Python code. This code can either be functions classes or variables. A Python module is a .py file containing executable code.
	Some of the commonly used built-in modules are:
	os
	sys
	math
	random
	data time
	JSON


Q. What is PEP 8?
	PEP stands for Python Enhancement Proposal. PEP 8 is a coding convention, a set of recommendations about how to write your Python code more readable.

Q. What is flake8?
	Flake8 is a Python library that wraps PyFlakes, pycodestyle and Ned Batchelder’s McCabe script. It is a great toolkit for checking your code base against coding style (PEP8), programming errors (like “library imported but unused” and “Undefined name”) and to check cyclomatic complexity.
	->pip install flake8
	Inside the Django project dir, run the command:
	->flake8
	Or you can pass the path to a file/dir:
	->flake8 bootcamp/feeds/

Q. How Python is interpreted? Is Python Compiled or Interpreted? 
	Python is an interpreted language. Python program runs directly from the source code. It converts the source code that is written by the programmer into an intermediate language, which is again translated into machine language that has to be executed.

Q. What are the tools that help to find bugs or perform static analysis?
	PyChecker is a static analysis tool that detects bugs in Python source code and warns about the style and complexity of the bug. Pylint is another tool that verifies whether the module meets the coding standard.

Q. How are the argument passed in python?(call by value or call by reference)?	
	Everything in Python is an object and all variables hold references to the objects. The references values are according to the functions; as a result, you cannot change the value of the references. However, you can change the objects if it is mutable.

	Pass by value: Copy of the actual object is passed. Changing the value of the copy of the object will not change the value of the original object.
	Pass by reference: Reference to the actual object is passed. Changing the value of the new object will change the value of the original object.
	In Python, arguments are passed by reference, i.e., reference to the actual object is passed.

	def appendNumber(arr):
		arr.append(4)

	arr = [1, 2, 3]

	print(arr)  #Output: => [1, 2, 3]
	appendNumber(arr)
	print(arr)  #Output: => [1, 2, 3, 4]
	
Q. What is lambda function in Python? when and why, where do we use it?
	In Python, anonymous function means that a function is without a name. As we already know that def keyword is used to define the normal functions and the lambda keyword is used to create anonymous functions. It has the following syntax:
	Lambda arguments: expression
	1. This function can have any number of arguments but only one expression, which is evaluated and returned.
	2. One is free to use lambda functions wherever function objects are required.
	Without using Lambda : Here, both of them returns the cube of a given number. But, while using def, we needed to define a function with a name cube and needed to pass a value to it. After execution, we also needed to return the result from where the function was called using the return keyword.
	Using Lambda : Lambda definition does not include a “return” statement, it always contains an expression which is returned. We can also put a lambda definition anywhere a function is expected, and we don’t have to assign it to a variable at all. This is the simplicity of lambda functions.

	def cube(y): 
		return y*y*y; 
	  
	g = lambda x: x*x*x 
	print(g(7)) 
	print(cube(5)) 


Q. What is the purpose of pass keyword in python?
	Pass means, no-operation Python statement, or in other words it is a placeholder in compound statement, where there should be a blank left and nothing has to be written there.

Q. What is unittest in Python?
	A unit testing framework in Python is known as unittest. It supports sharing of setups, automation testing, shutdown code for tests, aggregation of tests into collections etc.

Q. What are the negative index and why they used?
	Python sequences can be index in positive and negative numbers. For positive index, 0 is the first index, 1 is the second index and so forth. For negative index, (-1) is the last index and (-2) is the second last index and so forth.
	The negative index is used to remove any new-line spaces from the string and allow the string to except the last character that is given as S[:-1]. The negative index is also used to show the index to represent the string in correct order.

	The sequences in Python are indexed and it consists of the positive as well as negative numbers. The numbers that are positive uses ‘0’ that is uses as first index and ‘1’ as the second index and the process goes on like that.

	The index for the negative number starts from ‘-1’ that represents the last index in the sequence and ‘-2’ as the penultimate index and the sequence carries forward like the positive number.

	The negative index is used to remove any new-line spaces from the string and allow the string to except the last character that is given as S[:-1]. The negative index is also used to show the index to represent the string in correct order.


Q. Explain how can you make a python script executable in unix?
	To make a Python Script executable on Unix, you need to do two things,
		Script file's mode must be executable and
		the first line must begin with # ( #!/usr/local/bin/python)




Q. Purpose of "/" and "//" operator in python?
	Division ("/"):  Division works in Python the way it's mathematically defined.
	5 / 2 = 2.5
	Floor Division ("//"): The division of operands where the result is the quotient in which the digits after the decimal point are removed. But if one of the operands is negative, the result is floored, i.e., rounded away from zero (towards negative infinity). 
	 
	5//2=2
	-11//3 = -4



Q4. What is *args and **kwargs ?
	We use *args when we aren’t sure how many arguments are going to be passed to a function, or if we want to pass a stored list or tuple of arguments to a function. **kwargs is used when we don’t know how many keyword arguments will be passed to a function, or it can be used to pass the values of a dictionary as keyword arguments. The identifiers args and kwargs are a convention, you could also use *bob and **billy but that would not be wise.


Q5. What is pickling and unpickling in python?
	Pickle module accepts any Python object and converts it into a string representation and dumps it into a file by using dump function, this process is called pickling. While the process of retrieving original Python objects from the stored string representation is called unpickling.
	Python library offers a feature - serialization out of the box. Serializing a object refers to transforming it into a format that can be stored, so as to be able to deserialize it later on, to obtain the original object. Here, the pickle module comes into play.

	Pickling
	Pickling is the name of the serialization process in Python. Any object in Python can be serialized into a byte stream and dumped as a file in the memory. The process of pickling is compact but pickle objects can be compressed further. Moreover, pickle keeps track of the objects it has serialized and the serialization is portable across versions.
	The function used for the above process is pickle.dump().

	Unpickling
	Unpickling is the complete inverse of pickling. It deserializes the byte stream to recreate the objects stored in the file, and loads the object to memory.
	The function used for the above process is pickle.load().
	

Q7. What is the usage of help() and dir() function in Python?
	Ans: Help() and dir() both functions are accessible from the Python interpreter and used for viewing a consolidated dump of built-in functions. 
	Help() function: The help() function is used to display the documentation string and also facilitates you to see the help related to modules, keywords, attributes, etc.
	Dir() function: The dir() function is used to display the defined symbols.


Q8. Explain map reduce filter and zip function?
	map function executes the function given as the first argument on all the elements of the iterable given as the second argument. If the function given takes in more than 1 arguments, then many iterables are given. #Follow the link to know more similar functions.



Q10. In Python what is slicing?
	A mechanism to select a range of items from sequence types like list, tuple, strings etc. is known as slicing. 
	Syntax: list_name[start_index:end_index:step]
	[::-1] is used to reverse the order of an array or a sequence.




Q12. When will the else part of try-except-else be executed?
	The else part is executed when no exception occurs.








	




Q16. What is monkey patching. How to implement it in python?
	In Python, the term monkey patch only refers to dynamic modifications of a class or module at run-time.

	Consider the below example:
	# m.py
	class MyClass:
	def f(self):
	print "f()"

	We can then run the monkey-patch testing like this:
	import m
	def monkey_f(self):
	print "monkey_f()"
	 
	m.MyClass.f = monkey_f
	obj = m.MyClass()
	obj.f()

	The output will be as below:
	monkey_f()
	As we can see, we did make some changes in the behavior of f() in MyClass using the function we defined, monkey_f(), outside of the module m.


Q20. How memory is managed in Python?
	1. Python memory is managed by Python private heap space. All Python objects and data structures are located in a private heap. The programmer does not have an access to this private heap and interpreter takes care of this Python private heap.
	2. The allocation of Python heap space for Python objects is done by Python memory manager. The core API gives access to some tools for the programmer to code.
	3. Python also have an inbuilt garbage collector, which recycle all the unused memory and frees the memory and makes it available to the heap space.

Q21. Whenever Python exits, why isn’t all the memory de-allocated?
	1. Whenever Python exits, especially those Python modules which are having circular references to other objects or the objects that are referenced from the global namespaces are not always de-allocated or freed.
	2. It is impossible to de-allocate those portions of memory that are reserved by the C library.
	3. On exit, because of having its own efficient clean up mechanism, Python would try to de-allocate/destroy every other object.


Q13. Explain garbage collection in python?
	Python deletes unwanted objects (built-in types or class instances) automatically to free the memory space. The process by which Python periodically frees and reclaims blocks of memory that no longer are in use is called Garbage Collection.

	Python's garbage collector runs during program execution and is triggered when an object's reference count reaches zero. An object's reference count changes as the number of aliases that point to it changes.

	An object's reference count increases when it is assigned a new name or placed in a container (list, tuple, or dictionary). The object's reference count decreases when it's deleted with del, its reference is reassigned, or its reference goes out of scope. When an object's reference count reaches zero, Python collects it automatically.

	a = 40      # Create object <40> 
	b = a       # Increase ref. count  of <40>
	c = [b]     # Increase ref. count  of <40>
	del a       # Decrease ref. count  of <40>
	b = 100     # Decrease ref. count  of <40>
	c[0] = -1   # Decrease ref. count  of <40>


Q43.How can files be deleted in Python?
	Ans: To delete a file in Python, you need to import the OS Module. After that, you need to use the os.remove() function.
	import os
	os.remove("xyz.txt")




Q24. What is with expression?
	with statement is used to wrap the execution of a block of code within methods defined by the context manager.
	Context manager is a class that implements __enter__ and __exit__ methods. Use of with statement ensures that the __exit__ method is called at the end
	 of the nested block. This concept is similar to the use of try…finally block. 
	First the __enter__ method is called, then the code within with statement is executed and finally the __exit__ method is called. __exit__ method
	 is called even if there is an error. It basically closes the file stream.
	The with statement in Python ensures that cleanup code is executed when working with unmanaged resources by encapsulating common preparation and cleanup tasks. It may be used to open a file, do something, and then automatically close the file at the end. It may be used to open a database connection, do some processing, then automatically close the connection to ensure resources are closed and available for others. with will cleanup the resources even if an exception is thrown. This statement is like the using statement in C#.
	Consider you put some code in a try block, then in the finally block, you close any resources used. The with statement is like syntactic sugar for that.

	The syntax of this control-flow structure is:

	with expression [as variable]:
	….with-block

	>>> with open('data.txt') as data:


Q28. What are the generators in python?
	Ans: Functions that return an iterable set of items are called generators.

Q17: Why and when do you use generators in Python?
	A generator in Python is a function which returns an iterable object. We can iterate on the generator object using the yield keyword. But we can only do that once because their values don’t persist in memory, they get the values on the fly.

	Generators give us the ability to hold the execution of a function or a step as long as we want to keep it. However, here are a few examples where it is beneficial to use generators.
	1. We can replace loops with generators for efficiently calculating results involving large data sets.
	2. Generators are useful when we don’t want all the results and wish to hold back for some time.
	3. Instead of using a callback function, we can replace it with a generator. We can write a loop inside the function doing the same thing as the callback and turns it into a generator.



Q18: What does the yield keyword do in Python?
	The yield keyword can turn any function into a generator. It works like a standard return keyword. But it’ll always return a generator object. Also, a method can have multiple calls to the yield keyword.

	def testgen(index):
	  weekdays = ['sun','mon','tue','wed','thu','fri','sat']
	  yield weekdays[index]
	  yield weekdays[index+1]

	day = testgen(0)
	print next(day), next(day)
	#output: sun mon


Q23. What are python iterators?
	Ans: Iterators are objects which can be traversed though or iterated upon.

	Iterator is an object.
	It remembers its state i.e., where it is during iteration (see code below to see how)
	__iter__() method initializes an iterator.
	It has a __next__() method which returns the next item in iteration and points to the next element. Upon reaching the end of iterable object __next__() must return StopIteration exception.
	It is also self iterable.
	Iterators are objects with which we can iterate over iterable objects like lists, strings, etc.

Q25. What is closure?
	The technique by which some data ("Hello") gets attached to the code is called closure in Python.
	This value in the enclosing scope is remembered even when the variable goes out of scope or the functionEx itself is removed from the current namespace.
	Example:
	def outer_func2():
		message = 'Hi'
		
		def inner_func2():
			print(message)
		
		return inner_func2
	closure = outer_func2() # now closure is functionEx which is equal to inner_func2
	print(closure) # <functionEx outer_func2.<locals>.inner_func2 at 0x02DADC90>
	print(closure.__name__) #inner_func2
	closure()#hi
	print(outer_func2()) #<functionEx outer_func2.<locals>.inner_func2 at 0x0336DB70>

	#This value in the enclosing scope is remembered even when the variable goes out of scope or the functionEx itself is removed from the current namespace.
	del outer_func2
	closure() # hi


Q25. What is decorator?
	Python has an interesting feature called decorators to add functionality to an existing code.
	A decorator takes in a function, adds some functionality and returns it.
	We can see that the decorator function add some new functionality to the original function. This is similar to packing a gift. The decorator acts as a wrapper.
	The nature of the object that got decorated (actual gift inside) does not alter. But now, it looks pretty (since it got decorated)
	Example:

	def smart_divide(func):
		def inner(a,b):
			print("I am going to divide",a,"and",b)
			if b == 0:
				print("Whoops! cannot divide")
				return
			return func(a,b)
		return inner

	@smart_divide
	def divide(a,b):
		return a/b

	divide(2,5) 
	#I am going to divide 2 and 5
	#0.4

	divide(2,0)
	#I am going to divide 2 and 0
	#Whoops! cannot divide







Q. Features of python and its advantages and disadvantages?
	Python is an interpreted language. That means that, unlike languages like C and its variants, Python does not need to be compiled before it is run. Other interpreted languages include PHP and Ruby.
	Python is dynamically typed, this means that you don’t need to state the types of variables when you declare them or anything like that. You can do things like x=111 and then x="I'm a string" without error
	Python is well suited to object orientated programming in that it allows the definition of classes along with composition and inheritance. Python does not have access specifiers (like C++’s public, private).
	In Python, functions are first-class objects. This means that they can be assigned to variables, returned from other functions and passed into functions. Classes are also first class objects
	Writing Python code is quick but running it is often slower than compiled languages. Fortunately，Python allows the inclusion of C-based extensions so bottlenecks can be optimized away and often are. The numpy package is a good example of this, it’s really quite quick because a lot of the number-crunching it does isn’t actually done by Python
	Python finds use in many spheres – web applications, automation, scientific modeling, big data applications and many more. It’s also often used as “glue” code to get other languages and components to play nice.








Q. How you can convert a number to a string?
	In order to convert a number into a string, use the inbuilt function str(). If you want a octal or hexadecimal representation, use the inbuilt function oct() or hex().


Q. Explain how to delete a file in Python?
	By using a command os.remove (filename) or os.unlink(filename)


Q22. How can you randomize the items of a list in place in Python?
	Ans: Consider the example shown below:
	from random import shuffle
	x = ['Keep', 'The', 'Blue', 'Flag', 'Flying', 'High']
	shuffle(x)
	print(x)
	The output of the following code is as below.

	['Flying', 'Keep', 'Blue', 'High', 'The', 'Flag']
	
	
Q. Explain how can you generate random numbers in Python?
	The statement random.random() method return the floating point number that is in the range of [0, 1]. The function generates random float numbers. The methods that are used with the random class are the bound methods of the hidden instances. The instances of the Random can be done to show the multi-threading programs that creates a different instance of individual threads. The other random generators that are used in this are:

	randrange(a, b): it chooses an integer and define the range in-between [a, b]. It returns the elements by selecting it randomly from the range that is specified. It doesn’t build a range object.
	uniform(a, b): it chooses a floating point number that is defined in the range of [a,b].Iyt returns the floating point number
	normalvariate(mean, sdev): it is used for the normal distribution where the mu is a mean and the sdev is a sigma that is used for standard deviation.
	The Random class that is used and instantiated creates independent multiple random number generators.


Q. Explain how can you access a module written in Python from C?
	You can access a module written in Python from C by following method,
	Module = =PyImport_ImportModule("<modulename>");


Q. Mention five benefits of using Python?

	Python comprises of a huge standard library for most Internet platforms like Email, HTML, etc.
	Python does not require explicit memory management as the interpreter itself allocates the memory to new variables and free them automatically
	Provide easy readability due to use of square brackets
	Easy-to-learn for beginners
	Having the built-in data types saves programming time and effort from declaring variables

	Limitations of python
	Python’s interpreted nature imposes a speed penalty on it.
	While Python is great for a lot of things, it is weak in mobile computing, and in browsers.
	Being dynamically-typed, Python uses duck-typing (If it looks like a duck, it must be a duck). This can raise runtime errors.
	Python has underdeveloped database access layers. This renders it a less-than-perfect choice for huge database applications.
	And then, well, of course. Being easy makes it addictive. Once a Python-coder, always a Python coder.


Q. Is python case sensitive?
	Ans: Yes. Python is a case sensitive language.

Q12.What is type conversion in Python?
	Ans: Type conversion refers to the conversion of one data type iinto another.
	int() – converts any data type into integer type
	float() – converts any data type into float type
	ord() – converts characters into integer
	hex() – converts integers to hexadecimal
	oct() – converts integer to octal
	tuple() – This function is used to convert to a tuple.
	set() – This function returns the type after converting to set.
	list() – This function is used to convert any data type to a list type.
	dict() – This function is used to convert a tuple of order (key,value) into a dictionary.
	str() – Used to convert integer into a string.
	complex(real,imag) – This functionconverts real numbers to complex(real,imag) number.


Q14. Is indentation required in python?
	Ans: Indentation is necessary for Python. It specifies a block of code. All code within loops, classes, functions, etc is specified within an indented block. It is usually done using four space characters. If your code is not indented necessarily, it will not execute accurately and will throw errors as well.








Q22. How can the ternary operators be used in python?
	Ans: The Ternary operator is the operator that is used to show the conditional statements. This consists of the true or false values with a statement that has to be evaluated for it.

	Syntax:

	The Ternary operator will be given as:
	[on_true] if [expression] else [on_false]x, y = 25, 50big = x if x < y else y
	The expression gets evaluated like if x<y else y, in this case if x<y is true then the value is returned as big=x and if it is incorrect then big=y will be sent as a result.


Q40. Explain split(), sub(), subn() methods of “re” module in Python.
	Ans: To modify the strings, Python’s “re” module is providing 3 methods. They are:

	split() – uses a regex pattern to “split” a given string into a list.
	sub() – finds all substrings where the regex pattern matches and then replace them with a different string
	subn() – it is similar to sub() and also returns the new string along with the no. of replacements.





Q51. What is the process of compilation and linking in python?
	Ans: The compiling and linking allows the new extensions to be compiled properly without any error and the linking can be done only when it passes the compiled procedure. If the dynamic loading is used then it depends on the style that is being provided with the system. The python interpreter can be used to provide the dynamic loading of the configuration setup files and will rebuild the interpreter.

	The steps that are required in this as:

	Create a file with any name and in any language that is supported by the compiler of your system. For example file.c or file.cpp
	Place this file in the Modules/ directory of the distribution which is getting used.
	Add a line in the file Setup.local that is present in the Modules/ directory.
	Run the file using spam file.o
	After a successful run of this rebuild the interpreter by using the make command on the top-level directory.
	If the file is changed then run rebuildMakefile by using the command as ‘make Makefile’.
	
	


Q29. How do I create a .pyc file?
	When a module is imported for the first time (or when the source file has changed since the current compiled file was created) a .pyc file containing the compiled code should be created in a __pycache__ subdirectory of the directory containing the .py file. The .pyc file will have a filename that starts with the same name as the .py file, and ends with .pyc, with a middle component that depends on the particular python binary that created it. 
	While both files hold bytecode, .pyc is the compiled version of a Python file. It has platform-independent bytecode. Hence, we can execute it on any platform that supports the .pyc format. Python automatically generates it to improve performance(in terms of load time, not speed).




Q6. What is PYTHONPATH? What is the purpose of PYTHONPATH, PYTHONSTARTUP, PYTHONHOME, PYTHONCORE env variable? What is the purpose of PYTHONPATH environment variable?
	Ans: It is an environment variable which is used when a module is imported. Whenever a module is imported, PYTHONPATH is also looked up to check for the presence of the imported modules in various directories. The interpreter uses it to determine which module to load.

	
	PYTHONPATH - It has a role similar to PATH. This variable tells the Python interpreter where to locate the module files imported into a program. It should include the Python source library directory and the directories containing Python source code. PYTHONPATH is sometimes preset by the Python installer.

	What is the purpose of PYTHONSTARTUP environment variable?
	PYTHONSTARTUP - It contains the path of an initialization file containing Python source code. It is executed every time you start the interpreter. It is named as .pythonrc.py in Unix and it contains commands that load utilities or modify PYTHONPATH.

	What is the purpose of PYTHONCASEOK environment variable?
	PYTHONCASEOK - It is used in Windows to instruct Python to find the first case-insensitive match in an import statement. Set this variable to any value to activate it.

	What is the purpose of PYTHONHOME environment variable?
	PYTHONHOME - It is an alternative module search path. It is usually embedded in the PYTHONSTARTUP or PYTHONPATH directories to make switching module libraries easy.

	PYTHONSTARTUP: It contains the path of an initialization file having Python source code. It is executed every time we start the interpreter. It is named as .pythonrc.py in Unix, and it contains commands that load utilities or modify PYTHONPATH.
	PYTHONCASEOK: It is used in Windows to instruct Python to find the first case-insensitive match in an import statement. We can set this variable with any value to activate it.
	PYTHONHOME: It is an alternative module search path. It is usually embedded in PYTHONSTARTUP or PYTHONPATH directories to make switching of module libraries easy.


22. What do file-related modules in Python do? Can you name some file-related modules in Python?
	Python comes with some file-related modules that have functions to manipulate text files and binary files in a file system. These modules can be used to create text or binary files, update their content, copy, delete, and more.

	Some file-related modules are os, os.path, and shutil.os. The os.path module has functions to access the file system, while the shutil.os module can be used to copy or delete files.


35. Is Python fully object oriented?
	Python does follow an object-oriented programming paradigm and has all the basic OOPs concepts such as inheritance, polymorphism, and more, with the exception of access specifiers. Python doesn’t support strong encapsulation (adding a private keyword before data members). Although, it has a convention that can be used for data hiding, i.e., prefixing a data member with two underscores.





Q.42. How do you take input in Python?
	For taking input from the user, we have the function input(). In Python 2, we had another function raw_input().
	The input() function takes, as an argument, the text to be displayed for the task:
	>>> a=input('Enter a number')


Q-11: Write A Regular Expression That Confirms An Email Id Using The Python Reg Expression Module “Re”?
	Python has a regular expression module “re.”
	Check out the “re” expression that can check the email id for .com and .co.in subdomain.
	import re
	print(re.search(r"[0-9a-zA-Z.]+@[a-zA-Z]+\.(com|co\.in)$","micheal.pages@mp.com"))

	What Is The Purpose Of Id() Function In Python?
	The id() is one of the built-in functions in Python.

	Signature: id(object)
	It accepts one parameter and returns a unique identifier associated with the input object.


Q-36: What Does The __ Name __ Do In Python? 61. What is if __name__ == "__main__"? 
	The __name__ is a unique variable. Since Python doesn’t expose the main() function, so when its interpreter gets to run the script, it first executes the code which is at level 0 indentation.

	To see whether the main() gets called, we can use the __name__ variable in an if clause compares with the value “__main__.”


Q-37: What Is The Purpose Of “End” In Python?
	Python’s print() function always prints a newline in the end. The print() function accepts an optional parameter known as the ‘end.’ Its value is ‘\n’ by default. We can change the end character in a print statement with the value of our choice using this parameter.

	# Example: Print a  instead of the new line in the end.
	print("Let's learn" , end = ' ')  
	print("Python") 

	# Printing a dot in the end.
	print("Learn to code from techbeamers" , end = '.')  
	print("com", end = ' ')
	The output is:

	Let's learn Python
	Learn to code from techbeamers.com


Q-49: What Makes The CPython Different From Python?
	CPython has its core developed in C. The prefix ‘C’ represents this fact. It runs an interpreter loop used for translating the Python-ish code to C language.

Q-50: Which Package Is The Fastest Form Of Python?
	PyPy provides maximum compatibility while utilizing CPython implementation for improving its performance.

	The tests confirmed that PyPy is nearly five times faster than the CPython. It currently supports Python 2.7.


Q-52: How Is Python Thread Safe?
	Python ensures safe access to threads. It uses the GIL mutex to set synchronization. If a thread loses the GIL lock at any time, then you have to make the code thread-safe.

	For example, many of the Python operations execute as atomic such as calling the sort() method on a list.


Q13. How to install Python on Windows and set path variable?
	Ans: To install Python on Windows, follow the below steps:

	Install python from this link: https://www.python.org/downloads/
	After this, install it on your PC. Look for the location where PYTHON has been installed on your PC using the following command on your command prompt: cmd python. 
	Then go to advanced system settings and add a new variable and name it as PYTHON_NAME and paste the copied path.
	Look for the path variable, select its value and select ‘edit’.
	Add a semicolon towards the end of the value if it’s not present and then type %PYTHON_HOME% 


Q.1 What is PIP software in the Python world?
	Answer: PIP is an acronym for Python Installer Package which provides a seamless interface to install various Python modules. It is a command line tool which can search for packages over the internet and install them without any user interaction.


3. What is a dynamically typed language? What type of language is python? Programming or scripting?
	Before we understand what a dynamically typed language, we should learn about what typing is. Typing refers to type-checking in programming languages. In a strongly-typed  language, such as Python, "1" + 2 will result in a type error, since these languages don't allow for "type-coercion" (implicit conversion of data types). On the other hand, a weakly-typed  language, such as Javascript, will simply output "12" as result.

	Type-checking can be done at two stages -

	Static - Data Types are checked before execution.
	Dynamic - Data Types are checked during execution.
	Python being an interpreted language, executes each statement line by line and thus type-checking is done on the fly, during execution. Hence, Python is a Dynamically Typed language.


Q-93: What Is The Command To Debug A Python Program?
	The following command helps run a Python program in debug mode.

	$ python -m pdb python-script.py


Q-91: How Do You Debug A Program In Python? Is It Possible To Step Through The Python Code?
	Yes, we can use the Python debugger (pdb) to debug any Python program. And if we start a program using pdb, then it let us even step through the code.

Q-92: List Down Some Of The PDB Commands For Debugging Python Programs?
	Here are a few PDB commands to start debugging Python code.

	Add breakpoint (b)
	Resume execution (c)
	Step by step debugging (s)
	Move to the next line (n)
	List source code (l)
	Print an expression (p)
	w

Q. what the collections in python?
	counter
	orderedDict
	DefaultDict
	NamedTuple
	chainmap
	dequeue


78) What are the common examples of exceptions in Python?
	The common examples of exceptions in Python are:

	Division by Zero
	Accessing a file that does not exist.
	Addition of two incompatible types
	Trying to access a nonexistent index of a sequence
	Removing the table from the disconnected database server.
	ATM withdrawal of more than the available amount

79) Explain important Python errors

	The important Python errors are 1) ArithmeticError, 2) ImportError, and 3) IndexError.

	ArithmeticError: ArithmeticError act as a base class for all arithmetic exceptions. It is raised for errors in arithmetic operations.
	ImportError: ImportError is raised when you are trying to import a module which does not present. This kind of exception occurs if you have made a typing mistake in the module name or the module which is not present in the standard path.
	IndexError: An IndexError is raised when you try to refer a sequence which is out of range.

