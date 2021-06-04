## Installation and setup:
1. What is the recommended way to install Django?
	Installing using pip is the recommended way to install Django Framework. Below are the steps to install official release of Django with pip
	Install pip.
	Configure virtualenv and virtualenvwrapper
	Once virtual environment is created and activated, enter the command pip install Django to install Django

2. How to install the development version of Django
	Follow the below steps to Install the development version of Django Framework.
	Check out Django’s main development branch
	$ git clone https://github.com/django/django.git
	Make sure that the Python interpreter can load Django’s code. The most convenient way to do this is to use virtualenv, virtualenvwrapper, and pip.
	After setting up and activating the virtualenv, run the following command:
	$ pip install -e django/
	Source:https://docs.djangoproject.com/en/2.0/topics/install/

3. How to check installed version of Django?
	By running below command on Terminal.You can check installed version of Django Framework.
	py -m django --version

4. What is the latest and stable version of Django ?

5. List server requirement to install Django Framework.
	As Django is Python Framework, in order to install Django Python is required.Django comes with an inbuilt lightweight web server that you can use for the testing
	purpose.If you are using Django on production Apache with mod_wsgi is required.


## Basics of Django:
1. What do you understand by Django?
	Django is a free and open source web application framework, written in Python. Django is named after Django Reinhardt, Jazz guitarist from the 1930s to early 1950s who is one of the best guitarists of all time. Django was mainly developed to handle the intensive design of the newsroom. You can even build high-quality web applications using this. It adheres to the DRY principle and focuses completely on automating as much as possible.

	Django is high level python web framework, that encourage rapid development of web application, clean and pragmatic design. It let us build a high performance web application with less code quickly.
	Django focus on automating as much as possible and work on DRY principle.


2. What is DRY priciple.?
	In software engineering, don't repeat yourself (DRY)DRY is a principle of software development aimed at reducing repetition of software patterns, replacing them with abstractions; and several copies of the same data, using data normalization to avoid redundancy.
	The DRY principle is stated as "Every piece of knowledge must have a single, unambiguous, authoritative representation within a system"

2. Name the features available in Django web framework?
	Django is a high-level web application framework based on Python. This framework is one of the best in the industry for rapid development, pragmatic design without compromising on features.
	Some of the technical features of Django include:
	Below is the list of features offered by Django:

	A free, rich API
	Templating
	Form Handling
	Easy database migrations
	Internationalization
	Object Relational Mapping
	Testing Framework
	Session, user management, role-based permission
	Elegant URL design
	Cache System
	Code Reusability
	CDN Integration
	Security Features
	A huge number of third-party applications
	Admin Interface (CRUD)
	Fantastic Documentation

	1. Development Environment  Django comes with a lightweight web server to facilitate end-to-end application development and testing.
	2. Object-Relational Mapping (ORM) Support  Django provides a bridge between the data model and the database engine, and supports a large set of database systems including MySQL, Oracle, Postgres, etc.
	3. Multilingual Support  Django supports multilingual websites through its built-in internationalization system. So you can develop your website, which would support multiple languages.
	4. Administration GUI  Django provides a nice ready-to-use user interface for administrative activities. Save yourself the tedious work of creating interfaces for people to add and update content. Django does that automatically,
	5. Automatic database table creation. The migrate command is an elegant and distinctive feature of Django that looks at all your models and automatically creates tables in your database for any that don’t exist already.
	6. A powerful cache framework for dynamic websites. This system lets you cut down on expensive calculations by caching dynamic pages. There are a few levels of granularity here: You can cache individual pages or just the most expensive views to produce.


3. Is Django stable or not?
	Of course, Django is stable. Most of the companies are using it.

4. Is Django free?
	Yes, Django is free open source web framework for Python

5. When and who create Django?
	According to https://en.wikipedia.org/wiki/Django_(web_framework), Django was created in the fall of 2003, when the web programmers at the Lawrence Journal-World 
		newspaper, Adrian Holovaty and Simon Willison, began using Python to build applications. It was released publicly under a BSD license in July 2005. The 
		framework was named after guitarist Django Reinhardt.

6. What is the name of the Foundation which manages Django web framework?
	Django web framework is managed and maintained by an independent and non-profit organization named Django Software Foundation (DSF).

7. Is Django a high level or low-level framework?
	Django is a high-level Python’s web framework which was designed for rapid development and clean realistic design.

8. Why should Django be used for web development?

9. How is Django’s code reusability feature different from other frameworks?


9 Why is Django called a loosely coupled framework?
	Ans. Django is called a loosely coupled framework because of the MTV architecture it’s based on.
	Django’s architecture is a variant of MVC architecture and MTV is useful because it completely separates server code from the client’s machine.
	Django’s Models and Views are present on the client machine and only templates return to the client, which are essentially HTML, CSS code and contains the required data from the models.
	These components are totally different from each other and therefore, front-end developers and backend developers can work simultaneously on the project as these two parts changing will have little to no effect on each other when changed.
	Therefore, Django is a loosely coupled framework.


## Django Architecture:
Q1. Does Django Follow Architectural pattern?
	Yes, Django follows Model-View-Controller (MVC) architectural pattern.

Q2.Explain the architecture of Django?
	Django follows the MVT (Model View Template) pattern which is based on the Model View Controller architecture. It’s slightly different from the MVC pattern as it maintains its own conventions, so, the controller is handled by the framework itself. The template is a presentation layer. It is an HTML file mixed with Django Template Language (DTL). The developer provides the model, the view, and the template then maps it to a URL, and finally, Django serves it to the user.

	Django architecture consists of:
	Models: It describes your database schema and your data structure
	Views: It controls what a user sees, the view retrieves data from appropriate models and execute any calculation made to the data and pass it to the template
	Templates: It determines how the user sees it. It describes how the data received from the views should be changed or formatted for display on the page
	Controller: It is the heart of the system. It handles request and responses, setting up database connections and loading add-ons and specifies Django framework and URL parsing.

Q3. Explain the django project directory structure? 
	1. settings.py contains all the website settings. This is where we register any applications we create, the location of our static files, database configuration details, etc.  
	2. urls.py defines the site url-to-view mappings. While this could contain all the url mapping code, it is more common to delegate some of the mapping to particular applications, as you'll see later. 
	3. wsgi.py is used to help your Django application communicate with the web server. You can treat this as boilerplate.
	4. The manage.py : script is used to create applications, work with databases, and start the development web server. 

	•	A migrations folder, used to store "migrations" — files that allow you to automatically update your database as you modify your models. 
	•	_init_.py — An empty file that tells Python that this directory should be considered a Python package. It is an empty file created here so that Django/Python will recognise the folder as a Python Package and allow you to use its objects within other parts of the project. 

	admin.py  This file helps you make the app modifiable in the admin interface.

	models.py This is where all the application models are stored.

	tests.py  This is where your unit tests are.

	views.py  This is where your application views are.

4. What is the Controller in the MVC framework of Django?

Q5. What is the usage of Django-admin.py and manage.py?
	Django-admin.py: It is a Django’s command line utility for administrative tasks.
		
	Manage.py: It is an automatically created file in each Django project. It is a thin wrapper around the Django-admin.py. It has the following usage:
	It puts your project’s package on sys.path.
	It sets the DJANGO_SETTING_MODULE environment variable to points to your project’s setting.py file.

	Models.py file: This file defines your data model by extending your single code line into full database tables and add a pre-built administration section to manage content.
	Urls.py file: It uses a habitual expression to confine URL patterns for processing.
	Views.py file: It is the main part of Django. The actual processing happens in view.
	
26. What is the significance of manage.py file in Django?
	The manage.py file is automatically generated whenever you create a project. This is basically a command-line utility that helps you to interact with your Django
	project in various ways. It does the same things as django-admin but along with that, it also sets the DJANGO_SETTINGS_MODULE environment variable in order to point
	to your project’s settings. Usually, it is better to make use of manage.py rather than the django-admin in case you are working on a single project.

5. What is the difference between a Project and an App?
	An app is basically a Web Application that is created to do something for example, a database of employee records. A project, on the other hand, is a collection of apps of some particular website. Therefore, a single project can consist of ‘n’ number of apps and a single app can be in multiple projects.

6. What is the process of creating a project in Django? Explain the file structure of a typical Django project?
	1. Install django
	pip install django
	2. create project
	django-admin startproject mysite
	mysite/
		manage.py
		mysite/
			__init__.py
			settings.py
			urls.py
			wsgi.py

	3. run server
	python manage.py runserver
	4. go to 127.0.0.1:8000
7. Explain the importance of settings.py file and what data/ settings it contains.
8. What is the Usage of ALLOWED_HOST in Django project settings?

10. Why permanent redirecting is not a good option?

## Request and Response:
9. How a request is processed in Django?
	In Django whenever a request is made by a user, it goes through the following steps:
	Django determines the root URLconf module to use. Ordinarily, this is the value of the ROOT_URLCONF setting, but if the incoming HttpRequest object has a urlconf 
	attribute (set by middleware), its value will be used in place of the ROOT_URLCONF setting.
	Django loads that Python module and looks for the variable urlpatterns. This should be a Python list of django.urls.path() and/or django.urls.re_path() instances.
	Django runs through each URL pattern, in order, and stops at the first one that matches the requested URL.
	Once one of the URL patterns matches, Django imports and calls the given view, which is a simple Python function (or a class-based view). The view gets passed the 
	following arguments:
	An instance of HttpRequest.
	If the matched URL pattern returned no named groups, then the matches from the regular expression are provided as positional arguments.
	The keyword arguments are made up of any named parts matched by the path expression, overridden by any arguments specified in the optional kwargs argument 
	to django.urls.path() or django.urls.re_path().
	If no URL pattern matches, or if an exception is raised during any point in this process, Django invokes an appropriate error-handling view.

	When the user makes a request of your application, a WSGI handler is instantiated, which:
	imports your settings.py file and Django’s exception classes.
	loads all the middleware classes it finds in the MIDDLEWARE_CLASSES or MIDDLEWARES(depending on Django version) tuple located in settings.py
	builds four lists of methods which handle processing of request, view, response, and exception.
	loops through the request methods, running them in order
	resolves the requested URL
	loops through each of the view processing methods
	calls the view function (usually rendering a template)
	processes any exception methods
	loops through each of the response methods, (from the inside out, reverse order from request middlewares)
	finally builds a return value and calls the callback function to the web server
		
		
2. What is a context in Django?
	In Django Context is a dictionary with variable names in the form of key and value like {varible1: 101, varible2: 102},when we pass this context to the template 
	render method, {{ varible1 }} would be replaced with 101 and {{ varible2 }} with 102 in your template.

3. How to make a variable available to all the templates?
	You can make use of the RequestContext in case all your templates require the same objects, such as, in the case of menus. This method takes an HttpRequest as its 
	first parameter and it automatically populates the context with a few variables, according to the engine’s context_processors configuration option.


3. What is django.shortcuts.render function?
	When a View function returns a webpage as HttpResponse rather than a simple string, we use render().
	Render function is a shortcut function which lets the developer to easily pass the data dictionary with the template.
	This function then combines the template with data dictionary via templating engine.
	Finally, this render() returns an HttpResponse with the rendered text, which is the data returned by the models.
	Thus, Django render() bypasses lots of work for the developer and lets him use different templating engines.
	It is because this function provides the same functionality with other templating systems.
	The basic render Syntax:

	render(request, template_name, context=None, content_type=None, status=None, using=None)
	
	The request is the parameter which generates the response, the template_name containing the value where the template is stored.
	The template name and other parameters are for passing the dictionary.
	If you want more control, you can specify the content type, status of the data you passed and the render you are returning. That is the render().

4. How to get current page URI in Django template.
	You can use {{ request.path }} and {{ request.get_full_path }} to get current page URI in Django template.

30. Why is permanent redirection not a good option?
	Permanent redirection is used only when you don’t want to lead visitors to the old URLs. The response of the permanent redirections is cached by the browser so when 
	you try to redirect to something else it will cause issues. Since this is a browser-side operation if your user wants to move to a new page it will load the same page.


## Templates
1. What does the Django templates contain?
	A template is a simple text file. It can create any text-based format like XML, CSV, HTML, etc. A template contains variables that get replaced with values when the
	template is evaluated and tags (%tag%) that control the logic of the template.

2. How does Django Templating Work?

3. What is Jinja templating?
	Jinja Templating is a very popular templating engine for Python, the latest version is Jinja2. 

	Some of its features are:

	Sandbox Execution - This is a sandbox (or a protected) framework for automating the testing process
	HTML Escaping - It provides automatic HTML Escaping as <, >, & characters have special values in templates and if using a regular text, these symbols can lead 
	to XSS Attacks which Jinja deals with automatically.
	Template Inheritance
	Generates HTML templates much faster than default engine
	Easier to debug as compared to the default engine.

4. What are templates in Django or Django template language?
	Templates are an integral part of the Django MVT architecture. They generally comprise HTML, CSS, and js in which dynamic variables and information are embedded 
	with the help of views. Some constructs are recognized and interpreted by the template engine. The main ones are variables and tags.

	A template is rendered with a context. Rendering just replaces variables with their values, present in the context, and processes tags. Everything else remains as 
	it is.

	The syntax of the Django template language includes the following four constructs :

	Variables
	Tags
	Filters
	Comments
	To read more about templates you can refer to this: https://docs.djangoproject.com/en/3.1/topics/templates/

Q.15 How does Django Templating Work?
	Ans. Django Templates are Django’s answer to generate dynamic web pages. Templates, in general, are the HTML or the formats which can return as an Http response.
	Django templating engine handles templating in the Django framework.
	There are some template syntaxes which declares variables, control logic, filters, and comments.
	After putting these inside the HTML structure, when the web page is requested and called upon by the view function, the Django Template engine gets two things, the HTML structure with variables in place and the data to replace with those variables.
	It replaces the variables with data while also executing the control logic and generating filters.
	It renders the required HTML and sends it to the browser when all the work gets complete.

## Static Files:
1. How can you set up static files in Django?
	Basically, we require three main things to set up static files in Django:
	1) Set STATIC_ROOT in settings.py
	2) Run manage.py collect static
	3) Set up a Static Files entry on the PythonAnywhere web tab
	Make sure that django.contrib.staticfiles is included in your INSTALLED_APPS.
	In your settings file, define the STATIC_URL to the folder path string where your static files will be placed and make sure the folder exists.
	In your templates, use the static template tag to build the URL, for the given relative path using the configured STATICFILES_STORAGE.
	Store your static files in the static folder you specified. In addition to using a static directory inside your app, you can define a list of directories (STATICFILE_DIRS) in your settings file where Django will also look for static files.

	Ensure that django.contrib.staticfiles is added to your INSTALLED_APPS
	In your settings file. define STATIC_URL for ex.
	STATIC_URL = '/static/'
	In your Django templates, use the static template tag to create the URL for the given relative path using the configured STATICFILES_STORAGE.
	{% load static %}
	<img src="{% static 'my_sample/abcxy.jpg' %}" alt="ABC image">
	Store your static files in a folder called static in your app. For example my_sample/static/my_sample/abcxy.jpg

7. Define static files and explain their uses?
	Websites generally need to serve additional files such as images. Javascript or CSS. In Django, these files are referred to as “static files”, Apart from that Django 
	provides django.contrib.staticfiles to manage these static files.
	
3. What django collectstatic command does?
4. What is Static_root in Django?
	STATIC_ROOT is the absolute path to the directory from where Django collectstatic will static files for deployment.
	STATIC_ROOT example:
	STATIC_ROOT="/var/www/project_dir/static/"
	
5. Where to store static files in django ?


## Forms
1. What is ModelForm used for?

2. How to implement Forms validation?
3. What are different types of form available in django?

Q.9 What are custom validation rules in form data?
	Ans. Custom validation rules are the customized rules used for form validation. Suppose we have a feedback form. There are fields like messages, email, and subject. If we get message data of 1 or 2 words that are of no use to us. To check the issue, we use custom validation rules.

	We simply define a method in our forms.py by the name clean_message(). This is the Django way to do it. The method’s name for custom validation should start with a clean_fieldname(). Django form system automatically looks for this type of method.

	Thus, these are called custom validation rules in Django.

	It is always important to return the cleaned data of the field in a custom validation method. If not done, the method will return none instead resulting in loss of data.

Q.24 What are the various steps involved in form validation in Django?
	Ans. The form validation is a complex process comprising several steps. An end result is a form where all the data is either partially or fully clean. The form can also be completely wrong. Form validation is the process of validating data before performing any database operations.

	The steps involved in form validation include:

	The first method executed is to_python() method. It will convert the data into the appropriate Python type to perform validation.
	The second method is validate() method. It handles field-specific validation.
	The third method is run_validators() method. It calls all the field’s validators. The collective errors are then returned by this method.
	These three methods are actually executed in order. The clean() method calls all three methods in the appropriate order. This is a form class method. It calls all three to_python(), validate() & run_validators() methods. The comprised results and validation errors are returned.

	That’s how we get a cleaned form or validated form.


Q.25 What are some good practices when writing custom validators? How do we raise ValidationErrors as recommended by Django?
	Ans. Raising errors in Django shows how well planned a web-developer can be. There are certain ways recommended by Django to raise ValidationErrors.

	The ValidationErrors shall be descriptive and easy to comprehend.
	The error code shall be a descriptive one.
	Django encourages the use of the params parameter when returning variables.
	The params argument shall contain mapped data. Dictionaries are used in these cases.
	We use the gettext function or (_(‘text’)) to enable translation.



Q.15 What is the use of cached_property() decorator? (https://data-flair.training/blogs/django-interview-questions-and-answers/)

	Ans. The cached_property() decorator is a built-in decorator. This decorator comes under the django.utils.functional module. The decorator’s property is to take the 
	method as an argument. The method’s result is cached by the decorator for that instance.
	This is useful when a method is computationally expensive. Also, its generated value is valid for a while or for the session.
	We can use this decorator just before we define the computationally expensive method. That method’s answer is cached for the instance.


## Admin Interface
1. What is Django Admin Interface? Is Django’s Admin Interface customizable? If yes, then How?

35. What are the ways to customize the functionality of the Django admin interface?
	There are multiple ways to customize the functionality of the Django admin interface. You can piggyback on top of an add/change form that’s automatically generated
	by Django, you can add JavaScript modules using the js parameter. This parameter is basically a list of URLs that point to the JavaScript modules that are to be 
	included in your project within a <script> tag. You can also write views for the admin if you want.

13. How do we register a model with Django admin?
	To register a model with Django’s admin interface, we make changes to our apps admin.py file. We have to open the admin.py file in the app folder in which our
	models are. For example, if we have an app named ‘polls’ and we wish to register a model named ‘Question’, then we need to open
	‘polls/admin.py’ and import the Question model and write: 
		admin.site.register(Question). 
	This will register our Question model with the admin site.


## Unittesting
1. Which class do we inherit from in order to perform unit tests?
	We inherit from django.test.TestCase in order to perform unit tests as it contains all the methods we need to perform unit tests like assertEquals, assertTrue, etc.

2. What is the django.test.Client class used for?
	The Client class acts as a dummy web browser, allowing us to test our views and interact with our Django-powered application programmatically. This is especially helpful for doing integration testing.



## Views:

11. What are Django URLs?
	URLs are one of the most important parts of a web application and Django provides you with an elegant way to design your own custom URLs with help of its module known as URLconf (URL Configuration). The basic functionality of this python module is to 
	You can design your own URLs in Django in the way you like and then map them to the python function (View function). These URLs can be static as well as dynamic. These URLs as present in the urls.py where they are matched with the equivalent view function. 

	Basic Syntax:

	from django.urls import path
	from . import views
	urlpatterns = [
	   path('data/2020/', views.data_2020),
	   path('data/<int:year>/', views.data_year)
	]

Q.18 List some ways by which we can add our View functions to urls.py file?
	Ans. We can add our view to the main urls config in two ways:
	1. Adding a function View
	In this method, we import our view as function.
	We import the function itself from the particular view and then, add the particular URL to the urlpatterns list.

	2. Adding a Class-based view
	The class-based view is a more object-oriented approach.
	To begin, import the class from the views.py and then add the URL to the urlpatterns. This time we will need an inbuilt method to call the class as a view.

	In the name of the function on the previous method, write
	class_name.as_view()
	This will pass your view class as view function.
	Both class-based views and function-based views have their own pros and cons and we can use them in the appropriate situations to get the right results.

1 Give an example how you can write a VIEW in Django?
	Views are Django functions that take a request and return a response.  To write a view in Django we take a simple example of “Guru99_home” which uses the template Guru99_home.html and uses the date-time module to tell us what the time is whenever the page is refreshed.  The file we required to edit is called view.py, and it will be inside mysite/myapp/
	Copy the below code into it and save the file
	from datatime import datetime
	from django.shortcuts import render
	def home (request):
		return render(request, ‘Guru99_home.html’, {‘right_now’: datetime.utcnow()})
	Once you have determined the VIEW, you can uncomment this line in urls.py
	# url ( r ‘^$’ , ‘mysite.myapp.views.home’ , name ‘Guru99’),
	The last step will reload your web app so that the changes are noticed by the web server.


Q.1 What are views in Django ?
	A view is simply a Python function that takes a web(http) request and returns a web(http) response. This response can be HTML contents of a web page, or a redirect, or a 404 error, or an XML document, or an image, etc. 

	from django.http import HttpResponse
		def sample_function(request):
			return HttpResponse(“Welcome to Django”)
	
	There are two types of views:
	1. Function-Based Views: In this, we import our view as a function.
	2. Class-based Views: It’s an object-oriented approach.
	
3. What are different ways to create views in django?
4. What are Class-based views  and function based views in Django?
6. What is the difference between Function based and Class-based views?
5. What are generic views?
	When building a web application there are certain kind of views that we build again and again, such as a view that displays all records in the database (e.g., displaying all books in the books table), etc. These kinds of views perform the same functions and lead to repeated code. To solve this issue, Django uses class-based generic views. When using generic views, all we have to do is inherit the desired class from django.views.generic module and provide some information like model, context_object_name, etc.
7. Explain mixins in Django.
	A mixin is a special kind of multiple inheritances in Python. There are two main situations where mixins are used:
	You want to provide a lot of optional features for a class.
	You want to use one particular feature in a lot of different classes.
	Read More from https://stackoverflow.com/questions/533631/what-is-a-mixin-and-why-are-they-useful

	Mixin is a type of multiple inheritance wherein you can combine behaviors and attributes of more than one parent class. Mixins provide an excellent way to reuse code from multiple classes. For example, generic class-based views consist of a mixin called TemplateResponseMixin whose purpose is to define render_to_response() method. When this is combined with a class present in the View, the result will be a TemplateView class.
	One drawback of using these mixins is that it becomes difficult to analyze what a child class is doing and which methods to override in case of its code being too scattered between multiple classes.

8. What is Decorator? How to write custom decorator in Django ? Give one sample


## ORM and Migration:
24. How django convert many to many field in sql? or how many to many fields are stored in databases?

19. What is meant by lazy evaluation of a queryset?
	Django querysets doesn’t get evaluated straight off. Querysets will only be evaluated when they are actually needed, which means even if we add filter after filter to a queryset, it still wont run the actual query on the database. This behaviour optimizes the usage of the database to a great deal.

20. What is Queryset? what is the instance? (all, filter and get)?
	queryset is a collection of (sql) queries, in your example above print(b.query) will show you the sql query generated from your django filter calls.

2. Types of Model relationships in django ? List type of relationships/ asociations supported by Django.
4. What is GenericForeignKey ?
3. How to create custom sql query in django ?
	To create custom sql query ,use the database connection, call connection.cursor() to get a cursor object. Then, call cursor.execute(sql, [params]) to execute the SQL.

4. What is Django ORM? What is ORM? How it’s Important?
	This ORM (an acronym for Object Relational Mapper) enables us to interact with databases in a more pythonic way like we can avoid writing raw queries, it is possible to retrieve, save, delete and perform other operations over the database without ever writing any SQL query. It works as an abstraction layer between the models and the database.

5. What is __init__ method do in models?
6. What’s the difference between select_related and prefetch_related in Django ORM?
	Though both the functions are used to fetch the related fields on a model but their functioning is bit different from each other. In simple words, select_related uses
	a foreign key relationship, i.e. using join on the query itself while on the prefetch_related there is a separate lookup and the joining on the python side. 
	Let’s try to illustrate this via an example:

	from django.db import models
	class Country(models.Model):
		country_name = models.CharField(max_length=5)
	class State(models.Model):
		state_name = models.CharField(max_length=5)
		country = model.ForeignKey(Country)
	>> states = State.objects.select_related(‘country’).all()
	>> for state in states:
	…   print(state.state_name)  
	```Query Executed
	SELECT state_id, state_name, country_name FROM State INNER JOIN Country ON (State.country_id = Country.id)
	```
	>> country = Country.objects.prefetch_related(‘state’).get(id=1)
	>> for state in country.state.all():
	…   print(state.state_name)
	```Query Executed
	SELECT id, country_name FROM country WHERE id=1;
	SELECT state_id, state_name WHERE State WHERE country_id IN (1);
	```

34. How to obtain the SQL query from the queryset?
	print(queryset.query)

31. Difference between Django OneToOneField and ForeignKey Field?
	Both of them are of the most common types of fields used in Django. The only difference between these two is that ForeignKey field consists of on_delete option 
	along with a model’s class because it’s used for many-to-one relationships while on the other hand, the OneToOneField, only carries out a one-to-one relationship
	and requires only the model’s class.

32. How can you combine multiple QuerySets in a View?
	Initially, Concatenating QuerySets into lists is believed to be the easiest approach. Here’s an example of how to do that:
	from itertools import chain
	result_list = list(chain(model1_list, model2_list, model3_list))

7. Difference between Django’s annotate and aggregate methods?
8. When QuerySets are evaluated in Django?
	In Django, a QuerySet can be evaluated in Iteration, Slicing, Pickling/Caching, repr(),len(), list() and bool().

The pickle module is used for implementing binary protocols for serializing and de-serializing a Python object structure.
Pickling: It is a process where a Python object hierarchy is converted into a byte stream.
Unpickling: It is the inverse of Pickling process where a byte stream is converted into an object hierarchy.
	
9. What is a Model in Django and what is the Model class?

10. How can you fetch data from different databases inside the same view?
	While using a django queryset, the using(alias) function can be use to specify the database to fetch the query from. `alias` here refers to the db alias that is setup in the settings.DATABASES dictionary.

11. How to work with multiple databases in django? like one for saving and one for retrieving

23. When can you use iterators in Django ORM?
	Iterators in Python are basically containers that consist of a countable number of elements. Any object that is an iterator implements two methods which are, 
	the __init__() and the __next__()  methods. When you are making use of iterators in Django, the best situation to do it is when you have to process results that 
	will require a large amount of memory space. To do this, you can make use of the iterator() method which basically evaluates a QuerySet and returns the corresponding
	iterator over the results.


12. How to Configure Database in Django or Explain how you can set up the Database in Django?
	You can use the command edit mysite/setting.py , it is a normal python module with module level representing Django settings.
	Django uses SQLite by default; it is easy for Django users as such it won’t require any other type of installation. In the case your database choice is different
	that you have to the following keys in the DATABASE ‘default’ item to match your database connection settings
	
	Engines: you can change database by using ‘django.db.backends.sqlite3’ , ‘django.db.backeneds.mysql’, ‘django.db.backends.postgresql_psycopg2’,
		‘django.db.backends.oracle’ and so on
	Name: The name of your database. In the case if you are using SQLite as your database, in that case database will be a file on your computer, Name should be a full absolute path, including file name of that file.
	If you are not choosing SQLite as your database then setting like Password, Host, User, etc. must be added.


13. What does Of Django Field Class types do?
	Following points are specified by the Django Field Class type: 
	It specifies the database column type.
	It also specifies the default HTML widget which is availed while we render the form field.
	The requirements of the minimal validation which is used in Django admin is also specified by the field class.

14 Explain the migration in Django and how you can do in SQL?
	Migration in Django is to make changes to your models like deleting a model, adding a field, etc. into your database schema.  There are several commands you use to interact with migrations.
	Migrate
	Makemigrations
	Sqlmigrate
	To do the migration in SQL, you have to print the SQL statement for resetting sequences for a given app name.
	django-admin.py sqlsequencreset
	Use this command to generate SQL that will fix cases where a sequence is out sync with its automatically incremented field data.

15. Where are Django migrations stored?
	You can think Django Migrations as version control system for your database/Model. It keeps track of changes done in your application Models/Table like
	adding a field, deleting a model, etc. Migrations in Django are stored as an on-disk format, referred to here as “migration files”. These files are actually 
	just normal Python files with an agreed-upon object layout, written in a declarative style. A basic migration file looks like this:

	from django.db import migrations, models

	class Migration(migrations.Migration):

		dependencies = [('migrations', '0001_initial')]

		operations = [
			migrations.DeleteModel('Tribble'),
			migrations.AddField('Author', 'rating', models.IntegerField(default=0)),
		]
		
	Further Reading https://docs.djangoproject.com/en/2.0/topics/migrations/

16. List out the inheritance styles in Django?
	In Django, there is three possible inheritance styles
	1. Abstract base classes : Abstract base classes are useful when you want to put some common information into a number of other models. You write your base class
		and put abstract=True in the Meta class. This model will then not be used to create any database table. Instead, when it is used as a base class for other
		models, its fields will be added to those of the child class.
	2. Multi-table inheritance: The second type of model inheritance supported by Django is when each model in the hierarchy is a model all by itself. Each model
		corresponds to its own database table and can be queried and created individually. The inheritance relationship introduces links between the child model 
		and each of its parents (via an automatically-created OneToOneField). 
	3. Proxy models: You can use this model, If you only want to modify the Python level behavior of the model, without changing the model’s fields

17. List the database backends supported by Django Framework?
	Django officially supports four database backends, they are
	PostgreSQL
	MySQL
	SQLite
	Oracle
	In addition to these, you can also use following 3rd parties
	SAP SQL Anywhere
	IBM DB2
	Microsoft SQL Server
	Firebird
	ODBC

18. What is the difference between get() and filter() methods of a django queryset object?
	get() will fetch a single object whereas a filter() query will return multiple objects from the database using the lookup parameters. 
	get() raises exceptions when the number of objects found is not equal to 1.
	You can use any query expression with get(), just like with filter() - again, see Field lookups below.

	Note that there is a difference between using get(), and using filter() with a slice of [0]. If there are no results that match the query, get() will raise a
	DoesNotExist exception. This exception is an attribute of the model class that the query is being performed on - so in the code above, if there is no Entry
	object with a primary key of 1, Django will raise Entry.DoesNotExist.

	Similarly, Django will complain if more than one item matches the get() query. In this case, it will raise MultipleObjectsReturned, which again is an attribute 
	of the model class itself.

2. What is meant by lazy evaluation of a queryset?
	Django querysets doesn’t get evaluated straight off. Querysets will only be evaluated when they are actually needed,
	which means even if we add filter after filter to a queryset, it still wont run the actual query on the database. 
	This behaviour optimizes the usage of the database to a great deal.


21. How to override existing model class methods?
	There’s another set of model methods that encapsulate a bunch of database behavior that you’ll want to customize. In particular you’ll often want to change the way
	save() and delete() work.
	You’re free to override these methods (and any other model method) to alter behavior.
	A classic use-case for overriding the built-in methods is if you want something to happen whenever you save an object. 
	For example (see save() for documentation of the parameters it accepts):
	from django.db import models

	class Blog(models.Model):
		name = models.CharField(max_length=100)
		tagline = models.TextField()

		def save(self, *args, **kwargs):
			do_something()
			super().save(*args, **kwargs)  # Call the "real" save() method.
			do_something_else()
		
	Overridden model methods are not called on bulk operations
	Note that the delete() method for an object is not necessarily called when deleting objects in bulk using a QuerySet or as a result of a cascading
	delete(Model.delete() isn’t called on related models, but the pre_delete and post_delete signals are sent for all deleted objects.). To ensure customized delete logic gets executed, you can use pre_delete and/or post_delete signals.
	Unfortunately, there isn’t a workaround when creating or updating objects in bulk, since none of save(), pre_save, and post_save are called.

22. What is a Meta Class in Django?
	A Meta class is simply an inner class that provides metadata about the outer class in Django. It defines such things as available permissions,
	associated database table name, singular and plural versions of the name, etc.
	
23. What is model manager? Can we write custom manager? How and why?

	A Manager is an interface which provides database query operations to django models. A manager can be used to change the way a queryset behaves
	by adding custom operations on the queries.

	from django.db import models
	class User(models.Model):
		name = models.CharField(max_length=100)
		email = models.EmailField()

		def __str__(self):
			return self.name

24. What are models in Django?
	A model in Django refers to a class that maps to a database table or database collection. Each attribute of the Django model class represents a database field.
	They are defined in app/models.py

	Example: 

	from django.db import models
	class SampleModel(models.Model):
	field1 = models.CharField(max_length = 50)
	field2 = models.IntegerField()
	class Meta:
	db_table = “sample_model”
	Every model inherits from django.db.models.Model

	Our example has 2 attributes (1 char and 1 integer field), those will be in the table fields.

	The metaclass helps you set things like available permissions, singular and plural versions of the name, associated database table name, whether the model is abstract or not, etc.

	To get more information about models you can refer here: https://docs.djangoproject.com/en/3.1/topics/db/models/.


37. Explain Q objects in Django ORM?
	Q objects are used to write complex queries, as in filter() functions just `AND` the conditions while if you want to `OR` the conditions you can use Q objects.
	Let’s see an example:

	from django.db import models
	from django.db.models import Q
	>> objects = Models.objects.get(
	   Q(tag__startswith='Human'),
	   Q(category=’Eyes’) | Q(category=’Nose’)
	)
	```Query Executed
	SELECT * FROM Model WHERE tag LIKE ‘Human%’ AND (category=’Eyes’ OR category=’Nose’)
	```

37. Explain F objects in Django ORM?

## Caching:
1. List some caching strategies that you know in Django!
	Few caching strategies that are available in Django are as follows:

	File system caching
	In-memory caching
	Using Memcached
	Database caching
	
	Caching refers to the technique of storing the output results when they are processed initially so that next time when the same results are fetched again, instead of processing again those already stored results can be used, which leads to faster accessing as well us less resource utilization. Django provides us with a robust cache system that is able to store dynamic web pages so that these pages don’t need to be evaluated again for each request. 

	Some of the caching strategies in Django are listed below:

	Strategy	Description
	Memcached	A memory-based cache server is the fastest and most efficient
	FileSystem Caching	Values of the cache are stored as separate files in a serialized order
	Local-memory Caching	This is used as the default cache strategy by Django if you haven’t set anything. It is per-process as well as thread-safe.
	Database Caching 	Cache data will be stored in the database and works very well if you have a fast and well-indexed DB server.


## Signals:
1. What are signals in Django?
	Signal are inbuilt utility in Django. They allow to execute some piece of code based on some action or event is occurred in framework something like a new user 
	register, on delete of a record.
	Below is the list of some inbuilt signal in Django.
	django.db.models.signals.pre_save & django.db.models.signals.post_save : Sent before or after a model’s save() method is called.
	django.db.models.signals.pre_delete & django.db.models.signals.post_delete: Sent before or after a model’s delete() method or queryset’s delete() method is called.
	django.db.models.signals.m2m_changed : Sent when a ManyToManyField on a model is changed.
	django.core.signals.request_started & django.core.signals.request_finished :Sent when Django starts or finishes an HTTP request.
	
	Example:
	from django.contrib.auth.models import User
	from django.db.models.signals import post_save
	from django.dispatch import receiver
	@receiver(post_save, sender=User)
	def save_profile(sender, instance, **kwargs):
		instance.profile.save()


	Whenever there is a modification in a model, we may need to trigger some actions. 
	Django provides an elegant way to handle these in the form of signals. The signals are the utilities that allow us to associate events with actions.
	We can implement these by developing a function that will run when a signal calls it.

	List of built-in signals in the models:

	Signals	Description
	django.db.models.pre_init &
	django.db.models.post_init	Sent before or after a models’s _init_() method is called
	django.db.models.signals.pre_save & django.db.models.signals.post_save	Sent before or after a model’s save() method is called
	django.db.models.signals.pre_delete &
	django.db.models.signals.post_delete	Sent before or after a models’ delete() method or queryset delete() method is called
	django.db.models.signals.m2m_changed	Sent when a ManyToManyField is changed
	django.core.signals.request_started &
	django.core.signals.request_finished	Sent when an HTTP request is started or finished

2. What are the roles of receiver and sender in signals? or  What are the two important parameters in signals?
	The roles of receiver and sender in signals are:
	Receiver: It specifies the callback function which will be connected to the signal.
	Sender: It specifies a particular sender to receive a signal from.

	class Author(models.Model):
		full_name = models.CharField(max_length=100)
		short_name = models.CharField(max_length=50)

	class Book(models.Model):
		title = models.CharField(max_length=100)
		slug = models.SlugField(max_length=100)
		content = model.TextField()
		status = models.CharField(max_length=10, default=”Drafted”)
		author_id = model.PositiveIntegerField(null=True)
	In the above two models we are not having an author as foreignKey to Book model, so by default when the Author gets deleted it won’t delete all the Books
	written by the author. This is the case where signals come to picture, we can achieve this by using pre_delete or post_delete signals.

3. What are django signals? Give an example of post_save and pre_save signals.
	Django signals are used to notify other systems that certain actions have occurred at a point in the system, so that the other systems can act on them. In a simpler way, a sender notifies other receivers that have been registered with the sender that some action has taken place.
	There are a whole bunch of signals that can be setup which django provides. Signals can be pre save/post save signals on models, request started/request finished signals, pre migrate/post migrate signals on migrations among a big list of signals.
	Example of post save/post save signals
	from django.dispatch import receiver
	from django.db.models.signals import post_save
	from polls.models import MyModel

	@receiver(post_save, sender=MyModel, dispatch_uid="mymodel_post_save")
	def my_model_handler(sender, **kwargs):
	  print('Saved: {}'.format(kwargs['instance'].__dict__))

4. Custom signals
	signals.py
	import django.dispatch
	#user_signup_success
	user_email_changed = django.dispatch.Signal(providing_args=['user',])

	#sender
	user_email_changed.send(sender=update_user, user=user)

	#receiver
	@receiver(user_email_changed)
	def user_email_changed_verification(user, **kwargs):
		send_verification_email.delay(
				user, verification_attempt, reverify=True)
				
				
	# In signals.py
	import django.dispatch
	book_publised = django.dispatch.Signal(providing_args=["book", “author”])

	# In receivers.py
	from django.dispatch import receiver
	from .signals import *

	@receiver(book_publised)
	def send_mail_on_publish(sender, **kwargs):
		# contains the logic to send the email to author.
		
	We can dispatch signal anywhere as following.
	book_published.send(sender=Book, book=<Book Instance>, user=<Author Instance>)
	https://micropyramid.com/blog/using-djangos-built-in-signals-and-writing-custom-signals/





## Middlewares:
1. What is the use of middlewares in django? How to write a custom middleware?
	Middlewares are used to hook certain actions in the request response cycle. Middlewares can be used to perform operations on the request object before the view is executed or after the response object is created or just before the view is executed. Middlewares are executed in the order they are written in the settings file for django.
	
	Middleware is something that executes between the request and response. In simple words, you can say it acts as a bridge between the request and response. Similarly In Django when a request is made it moves through middlewares to views and data is passed through middleware as a response. 
	
2. How to write custom middleware in Django? give one sample( you can use IP filtering for the example)
	Writing a custom middleware
	https://simpleisbetterthancomplex.com/tutorial/2016/07/18/how-to-create-a-custom-django-middleware.html
	a Middleware is a regular Python class that hooks into Django’s request/response life cycle. Those classes holds pieces of code that are processed upon every request/response your Django application handles.

	The Middleware classes doesn’t have to subclass anything and it can live anywhere in your Python path. The only thing Django cares about is the path you register in the project settings MIDDLEWARE_CLASSES.
	Your Middleware class should define at least one of the following methods:
	Called during request:
	process_request(request)
	process_view(request, view_func, view_args, view_kwargs)
	Called during response:
	process_exception(request, exception) (only if the view raised an exception)
	process_template_response(request, response) (only for template responses)
	process_response(request, response)

	from datetime import datetime
	class BenchmarkMiddleware(object):
		def process_request(self, request):
			request._request_time = datetime.now()
		def process_template_response(self, request, response):
			response_time = request._request_time - datetime.now()
			response.context_data['response_time'] = abs(response_time)
			return response

2. What is the usage of middlewares in Django?
	Answer:
	Below are the usage of middlewares in Django:
	•Session management
	•Cross-site request forgery protection
	•Use authentication
	•Content Gzipping

3. What is some typical usage of middlewares in Django?
	Middleware is a function that acts on or transforms a request/response before/after it passes through the view layer (e.g. adding the user object to the request)
	Some usage of middlewares in Django is:
	It can be used for Session management,
	User authentication can be done with the help of this.
	It helps in Cross-site request forgery protection
	Content Gzipping, etc.



## Session:
1. What is the use of session framework in Django?
	The session framework helps you in storing and retrieving arbitrary data on a per-site visitor basis. The data is stored on the server side and abstracts the 
	receiving and sending of cookies. We can implement sessions through a piece of middleware.

	Django provides session that lets you store and retrive data on a per-site-visitor basis. Django abstract the process of sending and receiving the cookies,
	by placing a session id cookies on client side and storring all related that on the server side. So data itself is not stored client side. This is nice from a security perspective.
	
	Using the session framework, you can easily store and retrieve arbitrary data based on the pre-site-visitors. It stores data on the server-side and takes care of the process of sending and receiving cookies. These cookies just consist of a session ID, not the actual data itself unless you explicitly use a cookie-based backend.
	
2. How to set/unset session in Django?
	Setting Session in Django
	request.session['key'] = 'value'
	Unset Session in Django
	del request.session['key']

3. How to use file based sessions?
	You have to set the SESSION_ENGINE settings to “django.contrib.sessions.backends.file” to use file-based session.

4. What is the role of Cookie in Django?
	A cookie is a small piece of information which is stored in the client browser. It is used to store user's data in a file permanently (or for the specified time). Cookie has its expiry date and time and removes automatically when gets expire. Django provides built-in methods to set and fetch cookie.
	The set_cookie() method is used to set a cookie and get() method is used to get the cookie.
	The request.COOKIES['key'] array can also be used to get cookie values.
	from django.shortcuts import render  
	from django.http import HttpResponse  
	def setcookie(request):  
		response = HttpResponse("Cookie Set")  
		response.set_cookie('java-tutorial', 'javatpoint.com')  
		return response  
	def getcookie(request):  
		tutorial  = request.COOKIES['java-tutorial']  
		return HttpResponse("java tutorials @: "+  tutorial);  


## Authentication and authorisation:
16. Explain user authentication in Django?
	Django comes with a built-in user authentication system, which handles objects like users, groups, user-permissions, and few cookie-based user sessions. 
	Django User authentication not only authenticates the user but also authorizes him.

	The system consists and operates on these objects:

	Users
	Permissions
	Groups
	Password Hashing System
	Forms Validation
	A pluggable backend system

1. What is Authentication ?Explain user authentication in Django?
	Authentication is the process or action of verifying the identity of a user or process.

2. Types of Authentication in REST API ?
	Token based authentication and Session based authentication.

3. What is token based authentication system ?
4. How to implement social login authentication in Django ?
	Run the development server to make sure all is in order. The install 		python-social-auth using the pip install command. Update settings.py to include/register the library in the project  Update the database by  making migrations. Update the Project’s urlpatterns in urls.py to include the main auth URLs. Create a new app https://apps.twitter.com/app/new and make sure to use the callback url http://127.0.0.1:8000/complete/twitter. In the project directory, add a config.py file and grab the consumer key and consumer secret and add them to the config file. Finally add urls to the config file to specify the login and redirect urls. Do a sanity check and add friendly views.

5. How to implement JWT token:
	https://medium.com/python-pandemonium/json-web-token-based-authentication-in-django-b6dcfa42a332

	The default authentication schemes may be set globally, using the DEFAULT_AUTHENTICATION_CLASSES setting. For example.
	REST_FRAMEWORK = {
		'DEFAULT_AUTHENTICATION_CLASSES': (
			'rest_framework.authentication.BasicAuthentication',
			'rest_framework.authentication.SessionAuthentication',
		)
	}

	from rest_framework.authentication import SessionAuthentication, BasicAuthentication
	from rest_framework.permissions import IsAuthenticated
	from rest_framework.response import Response
	from rest_framework.views import APIView
	class ExampleView(APIView):
		authentication_classes = (SessionAuthentication, BasicAuthentication)
		permission_classes = (IsAuthenticated,)
		def get(self, request, format=None):
			content = {
				'user': unicode(request.user),  # `django.contrib.auth.User` instance.
				'auth': unicode(request.auth),  # None
			}
			return Response(content)

	Or, if you're using the @api_view decorator with function based views.
	@api_view(['GET'])
	@authentication_classes((SessionAuthentication, BasicAuthentication))
	@permission_classes((IsAuthenticated,))
	def example_view(request, format=None):
		content = {
			'user': unicode(request.user),  # `django.contrib.auth.User` instance.
			'auth': unicode(request.auth),  # None
		}
		return Response(content)

6. what is the use of authentication backend?   

7. Custom authentication:
	To implement a custom authentication scheme, subclass BaseAuthentication and override the .authenticate(self, request) method. The method should return a two-tuple of (user, auth) if authentication succeeds, or None otherwise.
	In some circumstances instead of returning None, you may want to raise an AuthenticationFailed exception from the .authenticate() method.
	from django.contrib.auth.models import User
	from rest_framework import authentication
	from rest_framework import exceptions

	class ExampleAuthentication(authentication.BaseAuthentication):
		def authenticate(self, request):
			username = request.META.get('X_USERNAME')
			if not username:
				return None

			try:
				user = User.objects.get(username=username)
			except User.DoesNotExist:
				raise exceptions.AuthenticationFailed('No such user')

			return (user, None)

8. Custom Permissions:
	create permissions.py file inside your app
	To implement a custom permission, override BasePermission and implement either, or both, of the following methods:
	.has_permission(self, request, view)
	.has_object_permission(self, request, view, obj)

	class IsInternal(permissions.BasePermission):
		def has_permission(self, request, view):
			api_key = None
			if not request.user.is_authenticated():
				api_key = request.META.get(
					'HTTP_AUTHORIZATION', None
				)
			if not api_key:
				if request.method == 'GET':
					api_key = request.GET.get('api_key', None)
				else:
					api_key = request.DATA.get('api_key', None)
			return api_key == INTERNAL_API_KEY






## Commands
1. Mention what command line can be used to load data into Django?
	To load data into Django you have to use the command line Django-admin.py loaddata. The command line will searches the data and loads the contents of the named fixtures into the database.
2. Explain what does django-admin.py makemessages command is used for?
	This command line executes over the entire source tree of the current directory and abstracts all the strings marked for translation.  It makes a message file in the locale directory.
3. What does the Django command `manage.py shell` do?
4. How to create super user in django ?
	In our project folder that contains Django’s manage.py script, we have to open the command prompt and type the python manage.py createsuperuser command. Then, we need to enter the username, the email, and finally the password, twice (for conformation). This will create a super user for our Django project.

## Deployment
1. How to setup django and apache in server ?
	It is done by using mod_wsgi. Make sure you have Apache and mod_wsgi installed.  Let’s say we want to share our project (myproject) with Apache.Set Apache to access our folder. Assume we put our myproject folder in the default “/var/www/html”. At this stage, accessing the project will be done via 127.0.0.1/myproject. Configure Apache in httpd.conf. By adding a <Files wsgi.py>  file configuration in it.


## Security
1. What is CSRF? How it’s preventing in Django?
2. What is Django Exception
3. What are the different types of Django Exception Classes?

Q46. What do you mean by the csrf_token?
	The csrf_token is used for protection against Cross-Site Request Forgeries. This kind of attack takes place when a malicious website consists of a link
	, some JavaScript or a form whose aim is to perform some action on your website by using the login credentials of a genuine user.


## Custom features:
1. How to create an Constant in Django.
	To create a constant in Django. Open your settings.py file and add a variable like MY_CONST = “MY_VALUE”.
	To use this constant in your views simply import setting like “Import settings in views.py” and use it as
	settings.MY_CONST
	
	constant.py
	CONST_VALUE = 'OK'
	from constants import ACCOUNT_LIMIT_OK

2. What is serialization in Django?
	Serialization is the process of converting Django models into other formats such as XML, JSON, etc.
	

## Exception

Q33. Give the exception classes present in Django.
	Django uses its own exceptions as well as those present in Python. Django core exceptions are present in django.core.exceptions class some of which are mentioned in the table below:

	Exception	Description
	AppRegistryNotReady

	Raised when you try to use your models before the app loading process (initializes the ORM) is completed.

	ObjectDoesNotExist

	This is the base class for DoesNotExist exceptions

	EmptyResultSet

	This exception may be raised if a query won’t return any result

	FieldDoesNotExist

	This exception is raised by a model’s _meta.get_field() function in case the requested field does not exist

	MultipleObjectsReturned

	This is raised by a query if multiple objects are returned and only one object was expected

## Some extra notes
Web Apps and Session Objects
cs 110 notes
Web apps sometimes need to remember information across multiple user requests. You can do this using a session object.
HTTP Requests are Stateless
Web requests are stateless. 'stateless' means 'memory-less'. The 'state' of the world-- all variables-- is lost on each request.
The server doesn't remember variables on each browser request. Your server code may have data members, but they're re-initialized on each request.
Session Variables
Session variables are the way to get around the statelessness of web requests.
Session variables remember data from request to request, and specifically for each user. Account info is one type of data stored in a session object.
Session variables live for a user session. Typically a user session will time out after some period of user inactivity (e.g., 30 minutes)
As session variables are user-specific, they cannot be used to share data between users-- for that the web app stores data in a database.

Session variables sometimes use cookies to record information. Cookies are little bits of information stored on the client's computer.
Session variables are generally key-value pairs.


The http.cookies module defines classes for abstracting the concept of cookies, an HTTP state management mechanism. It supports both simple string-only cookies, and provides an abstraction for having any serializable data-type as cookie value.

Note
On encountering an invalid cookie, CookieErroris raised, so if your cookie data comes from a browser you should always prepare for invalid data and catchCookieError on parsing.

Creating and Setting a Cookie

Cookies are used as state management, and as such as usually set by the server to be stored and returned by the client. The most trivial example of creating a cookie looks something like:

import Cookie c = Cookie.SimpleCookie() c['mycookie'] = 'cookie_value' print c 

The output is a valid Set-Cookie header ready to be passed to the client as part of the HTTP response:

$ python Cookie_setheaders.py Set-Cookie: mycookie=cookie_value 

Morsels

It is also possible to control the other aspects of a cookie, such as the expiration, path, and domain. In fact, all of the RFC attributes for cookies can be managed through the Morsel object representing the cookie value.


Limiting QuerySets

Negative indexing (i.e. Entry.objects.all()[-1]) is not supported.

fieldsets = (
        (None, {'fields': ('book','imprint', 'id')}),
        ('Availability', {'fields': ('status', 'due_back','borrower')}),
		)
		
