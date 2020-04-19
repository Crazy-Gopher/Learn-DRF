Building a form in Django
The Form class

We already know what we want our HTML form to look like. Our starting point for it in Django is this:
forms.py

A Form instance has an is_valid() method, which runs validation routines for all its fields. When this method is called, if all fields contain valid data, it will:

    return True
    place the form’s data in its cleaned_data attribute.




from django import forms
class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)

from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import NameForm

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'name.html', {'form': form})


Documentation
Search:

    Language: en

    Documentation version: 2.2

Working with forms¶

About this document

This document provides an introduction to the basics of web forms and how they are handled in Django. For a more detailed look at specific areas of the forms API, see The Forms API, Form fields, and Form and field validation.

Unless you’re planning to build websites and applications that do nothing but publish content, and don’t accept input from your visitors, you’re going to need to understand and use forms.

Django provides a range of tools and libraries to help you build forms to accept input from site visitors, and then process and respond to the input.
HTML forms¶

In HTML, a form is a collection of elements inside <form>...</form> that allow a visitor to do things like enter text, select options, manipulate objects or controls, and so on, and then send that information back to the server.

Some of these form interface elements - text input or checkboxes - are fairly simple and are built into HTML itself. Others are much more complex; an interface that pops up a date picker or allows you to move a slider or manipulate controls will typically use JavaScript and CSS as well as HTML form <input> elements to achieve these effects.

As well as its <input> elements, a form must specify two things:

    where: the URL to which the data corresponding to the user’s input should be returned
    how: the HTTP method the data should be returned by

As an example, the login form for the Django admin contains several <input> elements: one of type="text" for the username, one of type="password" for the password, and one of type="submit" for the “Log in” button. It also contains some hidden text fields that the user doesn’t see, which Django uses to determine what to do next.

It also tells the browser that the form data should be sent to the URL specified in the <form>’s action attribute - /admin/ - and that it should be sent using the HTTP mechanism specified by the method attribute - post.

When the <input type="submit" value="Log in"> element is triggered, the data is returned to /admin/.
GET and POST¶

GET and POST are the only HTTP methods to use when dealing with forms.

Django’s login form is returned using the POST method, in which the browser bundles up the form data, encodes it for transmission, sends it to the server, and then receives back its response.

GET, by contrast, bundles the submitted data into a string, and uses this to compose a URL. The URL contains the address where the data must be sent, as well as the data keys and values. You can see this in action if you do a search in the Django documentation, which will produce a URL of the form https://docs.djangoproject.com/search/?q=forms&release=1.

GET and POST are typically used for different purposes.

Any request that could be used to change the state of the system - for example, a request that makes changes in the database - should use POST. GET should be used only for requests that do not affect the state of the system.

GET would also be unsuitable for a password form, because the password would appear in the URL, and thus, also in browser history and server logs, all in plain text. Neither would it be suitable for large quantities of data, or for binary data, such as an image. A Web application that uses GET requests for admin forms is a security risk: it can be easy for an attacker to mimic a form’s request to gain access to sensitive parts of the system. POST, coupled with other protections like Django’s CSRF protection offers more control over access.

On the other hand, GET is suitable for things like a web search form, because the URLs that represent a GET request can easily be bookmarked, shared, or resubmitted.
Django’s role in forms¶

Handling forms is a complex business. Consider Django’s admin, where numerous items of data of several different types may need to be prepared for display in a form, rendered as HTML, edited using a convenient interface, returned to the server, validated and cleaned up, and then saved or passed on for further processing.

Django’s form functionality can simplify and automate vast portions of this work, and can also do it more securely than most programmers would be able to do in code they wrote themselves.

Django handles three distinct parts of the work involved in forms:

    preparing and restructuring data to make it ready for rendering
    creating HTML forms for the data
    receiving and processing submitted forms and data from the client

It is possible to write code that does all of this manually, but Django can take care of it all for you.
Forms in Django¶

We’ve described HTML forms briefly, but an HTML <form> is just one part of the machinery required.

In the context of a Web application, ‘form’ might refer to that HTML <form>, or to the Django Form that produces it, or to the structured data returned when it is submitted, or to the end-to-end working collection of these parts.
The Django Form class¶

At the heart of this system of components is Django’s Form class. In much the same way that a Django model describes the logical structure of an object, its behavior, and the way its parts are represented to us, a Form class describes a form and determines how it works and appears.

In a similar way that a model class’s fields map to database fields, a form class’s fields map to HTML form <input> elements. (A ModelForm maps a model class’s fields to HTML form <input> elements via a Form; this is what the Django admin is based upon.)

A form’s fields are themselves classes; they manage form data and perform validation when a form is submitted. A DateField and a FileField handle very different kinds of data and have to do different things with it.

A form field is represented to a user in the browser as an HTML “widget” - a piece of user interface machinery. Each field type has an appropriate default Widget class, but these can be overridden as required.
Instantiating, processing, and rendering forms¶

When rendering an object in Django, we generally:

    get hold of it in the view (fetch it from the database, for example)
    pass it to the template context
    expand it to HTML markup using template variables

Rendering a form in a template involves nearly the same work as rendering any other kind of object, but there are some key differences.

In the case of a model instance that contained no data, it would rarely if ever be useful to do anything with it in a template. On the other hand, it makes perfect sense to render an unpopulated form - that’s what we do when we want the user to populate it.

So when we handle a model instance in a view, we typically retrieve it from the database. When we’re dealing with a form we typically instantiate it in the view.

When we instantiate a form, we can opt to leave it empty or pre-populate it, for example with:

    data from a saved model instance (as in the case of admin forms for editing)
    data that we have collated from other sources
    data received from a previous HTML form submission

The last of these cases is the most interesting, because it’s what makes it possible for users not just to read a website, but to send information back to it too.
Building a form¶
The work that needs to be done¶

Suppose you want to create a simple form on your website, in order to obtain the user’s name. You’d need something like this in your template:

<form action="/your-name/" method="post">
    <label for="your_name">Your name: </label>
    <input id="your_name" type="text" name="your_name" value="{{ current_name }}">
    <input type="submit" value="OK">
</form>

This tells the browser to return the form data to the URL /your-name/, using the POST method. It will display a text field, labeled “Your name:”, and a button marked “OK”. If the template context contains a current_name variable, that will be used to pre-fill the your_name field.

You’ll need a view that renders the template containing the HTML form, and that can supply the current_name field as appropriate.

When the form is submitted, the POST request which is sent to the server will contain the form data.

Now you’ll also need a view corresponding to that /your-name/ URL which will find the appropriate key/value pairs in the request, and then process them.

This is a very simple form. In practice, a form might contain dozens or hundreds of fields, many of which might need to be pre-populated, and we might expect the user to work through the edit-submit cycle several times before concluding the operation.

We might require some validation to occur in the browser, even before the form is submitted; we might want to use much more complex fields, that allow the user to do things like pick dates from a calendar and so on.

At this point it’s much easier to get Django to do most of this work for us.
Building a form in Django¶
The Form class¶

We already know what we want our HTML form to look like. Our starting point for it in Django is this:
forms.py¶

from django import forms

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)

This defines a Form class with a single field (your_name). We’ve applied a human-friendly label to the field, which will appear in the <label> when it’s rendered (although in this case, the label we specified is actually the same one that would be generated automatically if we had omitted it).

The field’s maximum allowable length is defined by max_length. This does two things. It puts a maxlength="100" on the HTML <input> (so the browser should prevent the user from entering more than that number of characters in the first place). It also means that when Django receives the form back from the browser, it will validate the length of the data.

A Form instance has an is_valid() method, which runs validation routines for all its fields. When this method is called, if all fields contain valid data, it will:

    return True
    place the form’s data in its cleaned_data attribute.

The whole form, when rendered for the first time, will look like:

<label for="your_name">Your name: </label>
<input id="your_name" type="text" name="your_name" maxlength="100" required>

Note that it does not include the <form> tags, or a submit button. We’ll have to provide those ourselves in the template.
The view¶

Form data sent back to a Django website is processed by a view, generally the same view which published the form. This allows us to reuse some of the same logic.

To handle the form we need to instantiate it in the view for the URL where we want it to be published:
views.py¶

from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import NameForm

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'name.html', {'form': form})

If we arrive at this view with a GET request, it will create an empty form instance and place it in the template context to be rendered. This is what we can expect to happen the first time we visit the URL.

If the form is submitted using a POST request, the view will once again create a form instance and populate it with data from the request: form = NameForm(request.POST) This is called “binding data to the form” (it is now a bound form).

We call the form’s is_valid() method; if it’s not True, we go back to the template with the form. This time the form is no longer empty (unbound) so the HTML form will be populated with the data previously submitted, where it can be edited and corrected as required.

If is_valid() is True, we’ll now be able to find all the validated form data in its cleaned_data attribute. We can use this data to update the database or do other processing before sending an HTTP redirect to the browser telling it where to go next.



<form action="/your-name/" method="post">
    {% csrf_token %}
    {{ form }}
    <input type="submit" value="Submit">
</form>








path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
path('post/new/', views.post_new, name='post_new'),

from django import forms
from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})



from myapp.forms import LoginForm

def login(request):
   username = "not logged in"

   if request.method == "POST":
      #Get the posted form
      MyLoginForm = LoginForm(request.POST)

      if MyLoginForm.is_valid():
         username = MyLoginForm.cleaned_data['username']
   else:
      MyLoginForm = Loginform()

   return render(request, 'loggedin.html', {"username" : username})

      <form name = "form" action = "{% url "myapp.views.login" %}" method = "POST" >{% csrf_token %}

url(r'^login/', 'login', name = 'login'))



from django import forms
from myapp.models import Student

class EmpForm(forms.ModelForm):
                class Meta:
                                model = Student
                                fields = "__all__"

<form method="POST" class="post-form">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit" class="save btn btn-default">Save</button>
    </form>

here are other output options though for the <label>/<input> pairs:

    {{ form.as_table }} will render them as table cells wrapped in <tr> tags
    {{ form.as_p }} will render them wrapped in <p> tags
    {{ form.as_ul }} will render them wrapped in <li> tags


Django provides built-in methods to validate form data automatically. Django forms submit only if it contains CSRF tokens. It uses uses a clean and easy approach to validate data.

The is_valid()


Bound and unbound forms¶

A Form instance is either bound to a set of data, or unbound.

    If it’s bound to a set of data, it’s capable of validating that data and rendering the form as HTML with the data displayed in the HTML.
    If it’s unbound, it cannot do validation (because there’s no data to validate!), but it can still render the blank form as HTML.

>>> f = ContactForm()
>>> f.is_bound
False
>>> f = ContactForm({'subject': 'hello'})
>>> f.is_bound
True



Form.is_valid()¶

The primary task of a Form object is to validate data. With a bound Form instance, call the is_valid() method to run validation and return a boolean designating whether the data was valid:

>>> data = {'subject': 'hello',
...         'message': 'Hi there',
...         'sender': 'foo@example.com',
...         'cc_myself': True}
>>> f = ContactForm(data)
>>> f.is_valid()
True

s try with some invalid data. In this case, subject is blank (an error, because all fields are required by default) and sender is not a valid email address:

>>> data = {'subject': '',
...         'message': 'Hi there',
...         'sender': 'invalid email address',
...         'cc_myself': True}
>>> f = ContactForm(data)
>>> f.is_valid()
False


Form.errors¶

Access the errors attribute to get a dictionary of error messages:

>>> f.errors
{'sender': ['Enter a valid email address.'], 'subject': ['This field is required.']}

Documentation
Search:

    Language: en

    Documentation version: 2.2

The Forms API¶

About this document

This document covers the gritty details of Django’s forms API. You should read the introduction to working with forms first.
Bound and unbound forms¶

A Form instance is either bound to a set of data, or unbound.

    If it’s bound to a set of data, it’s capable of validating that data and rendering the form as HTML with the data displayed in the HTML.
    If it’s unbound, it cannot do validation (because there’s no data to validate!), but it can still render the blank form as HTML.

class Form[source]¶

To create an unbound Form instance, simply instantiate the class:

>>> f = ContactForm()

To bind data to a form, pass the data as a dictionary as the first parameter to your Form class constructor:

>>> data = {'subject': 'hello',
...         'message': 'Hi there',
...         'sender': 'foo@example.com',
...         'cc_myself': True}
>>> f = ContactForm(data)

In this dictionary, the keys are the field names, which correspond to the attributes in your Form class. The values are the data you’re trying to validate. These will usually be strings, but there’s no requirement that they be strings; the type of data you pass depends on the Field, as we’ll see in a moment.

Form.is_bound¶

If you need to distinguish between bound and unbound form instances at runtime, check the value of the form’s is_bound attribute:

>>> f = ContactForm()
>>> f.is_bound
False
>>> f = ContactForm({'subject': 'hello'})
>>> f.is_bound
True

Note that passing an empty dictionary creates a bound form with empty data:

>>> f = ContactForm({})
>>> f.is_bound
True

If you have a bound Form instance and want to change the data somehow, or if you want to bind an unbound Form instance to some data, create another Form instance. There is no way to change data in a Form instance. Once a Form instance has been created, you should consider its data immutable, whether it has data or not.
Using forms to validate data¶

Form.clean()¶

Implement a clean() method on your Form when you must add custom validation for fields that are interdependent. See Cleaning and validating fields that depend on each other for example usage.

Form.is_valid()¶

The primary task of a Form object is to validate data. With a bound Form instance, call the is_valid() method to run validation and return a boolean designating whether the data was valid:

>>> data = {'subject': 'hello',
...         'message': 'Hi there',
...         'sender': 'foo@example.com',
...         'cc_myself': True}
>>> f = ContactForm(data)
>>> f.is_valid()
True

Let’s try with some invalid data. In this case, subject is blank (an error, because all fields are required by default) and sender is not a valid email address:

>>> data = {'subject': '',
...         'message': 'Hi there',
...         'sender': 'invalid email address',
...         'cc_myself': True}
>>> f = ContactForm(data)
>>> f.is_valid()
False

Form.errors¶

Access the errors attribute to get a dictionary of error messages:

>>> f.errors
{'sender': ['Enter a valid email address.'], 'subject': ['This field is required.']}

In this dictionary, the keys are the field names, and the values are lists of strings representing the error messages. The error messages are stored in lists because a field can have multiple error messages.

You can access errors without having to call is_valid() first. The form’s data will be validated the first time either you call is_valid() or access errors.

The validation routines will only get called once, regardless of how many times you access errors or call is_valid(). This means that if validation has side effects, those side effects will only be triggered once.

Form.errors.as_data()¶

Returns a dict that maps fields to their original ValidationError instances.

>>> f.errors.as_data()
{'sender': [ValidationError(['Enter a valid email address.'])],
'subject': [ValidationError(['This field is required.'])]}

Use this method anytime you need to identify an error by its code. This enables things like rewriting the error’s message or writing custom logic in a view when a given error is present. It can also be used to serialize the errors in a custom format (e.g. XML); for instance, as_json() relies on as_data().

The need for the as_data() method is due to backwards compatibility. Previously ValidationError instances were lost as soon as their rendered error messages were added to the Form.errors dictionary. Ideally Form.errors would have stored ValidationError instances and methods with an as_ prefix could render them, but it had to be done the other way around in order not to break code that expects rendered error messages in Form.errors.

Form.errors.as_json(escape_html=False)¶

Returns the errors serialized as JSON.

>>> f.errors.as_json()
{"sender": [{"message": "Enter a valid email address.", "code": "invalid"}],
"subject": [{"message": "This field is required.", "code": "required"}]}

By default, as_json() does not escape its output. If you are using it for something like AJAX requests to a form view where the client interprets the response and inserts errors into the page, you’ll want to be sure to escape the results on the client-side to avoid the possibility of a cross-site scripting attack. It’s trivial to do so using a JavaScript library like jQuery - simply use $(el).text(errorText) rather than .html().

If for some reason you don’t want to use client-side escaping, you can also set escape_html=True and error messages will be escaped so you can use them directly in HTML.

Form.errors.get_json_data(escape_html=False)¶

Returns the errors as a dictionary suitable for serializing to JSON. Form.errors.as_json() returns serialized JSON, while this returns the error data before it’s serialized.

The escape_html parameter behaves as described in Form.errors.as_json().

Form.add_error(field, error)¶

This method allows adding errors to specific fields from within the Form.clean() method, or from outside the form altogether; for instance from a view.

The field argument is the name of the field to which the errors should be added. If its value is None the error will be treated as a non-field error as returned by Form.non_field_errors().

The error argument can be a simple string, or preferably an instance of ValidationError. See Raising ValidationError for best practices when defining form errors.

Note that Form.add_error() automatically removes the relevant field from cleaned_data.

Form.has_error(field, code=None)¶

This method returns a boolean designating whether a field has an error with a specific error code. If code is None, it will return True if the field contains any errors at all.

To check for non-field errors use NON_FIELD_ERRORS as the field parameter.

Form.non_field_errors()¶

This method returns the list of errors from Form.errors that aren’t associated with a particular field. This includes ValidationErrors that are raised in Form.clean() and errors added using Form.add_error(None, "...").
Behavior of unbound forms¶

It’s meaningless to validate a form with no data, but, for the record, here’s what happens with unbound forms:

>>> f = ContactForm()
>>> f.is_valid()
False
>>> f.errors
{}

Dynamic initial values¶

Form.initial¶

Use initial to declare the initial value of form fields at runtime. For example, you might want to fill in a username field with the username of the current session.

To accomplish this, use the initial argument to a Form. This argument, if given, should be a dictionary mapping field names to initial values. Only include the fields for which you’re specifying an initial value; it’s not necessary to include every field in your form. For




example:
>>> from django import forms
>>> class CommentForm(forms.Form):
...     name = forms.CharField(initial='class')
...     url = forms.URLField()
...     comment = forms.CharField()
>>> f = CommentForm(initial={'name': 'instance'}, auto_id=False)
>>> print(f)
<tr><th>Name:</th><td><input type="text" name="name" value="instance" required></td></tr>
<tr><th>Url:</th><td><input type="url" name="url" required></td></tr>
<tr><th>Comment:</th><td><input type="text" name="comment" required></td></tr>
>>> f = ContactForm(initial={'subject': 'Hi there!'})


Documentation
Search:

   Language: en

    Documentation version: 2.2

The Forms API¶

About this document

This document covers the gritty details of Django’s forms API. You should read the introduction to working with forms first.
Bound and unbound forms¶

A Form instance is either bound to a set of data, or unbound.

    If it’s bound to a set of data, it’s capable of validating that data and rendering the form as HTML with the data displayed in the HTML.
    If it’s unbound, it cannot do validation (because there’s no data to validate!), but it can still render the blank form as HTML.

class Form[source]¶

To create an unbound Form instance, simply instantiate the class:

>>> f = ContactForm()

To bind data to a form, pass the data as a dictionary as the first parameter to your Form class constructor:

>>> data = {'subject': 'hello',
...         'message': 'Hi there',
...         'sender': 'foo@example.com',
...         'cc_myself': True}
>>> f = ContactForm(data)

In this dictionary, the keys are the field names, which correspond to the attributes in your Form class. The values are the data you’re trying to validate. These will usually be strings, but there’s no requirement that they be strings; the type of data you pass depends on the Field, as we’ll see in a moment.

Form.is_bound¶

If you need to distinguish between bound and unbound form instances at runtime, check the value of the form’s is_bound attribute:

>>> f = ContactForm()
>>> f.is_bound
False
>>> f = ContactForm({'subject': 'hello'})
>>> f.is_bound
True

Note that passing an empty dictionary creates a bound form with empty data:

>>> f = ContactForm({})
>>> f.is_bound
True

If you have a bound Form instance and want to change the data somehow, or if you want to bind an unbound Form instance to some data, create another Form instance. There is no way to change data in a Form instance. Once a Form instance has been created, you should consider its data immutable, whether it has data or not.
Using forms to validate data¶

Form.clean()¶

Implement a clean() method on your Form when you must add custom validation for fields that are interdependent. See Cleaning and validating fields that depend on each other for example usage.

Form.is_valid()¶

The primary task of a Form object is to validate data. With a bound Form instance, call the is_valid() method to run validation and return a boolean designating whether the data was valid:

>>> data = {'subject': 'hello',
...         'message': 'Hi there',
...         'sender': 'foo@example.com',
...         'cc_myself': True}
>>> f = ContactForm(data)
>>> f.is_valid()
True

Let’s try with some invalid data. In this case, subject is blank (an error, because all fields are required by default) and sender is not a valid email address:

>>> data = {'subject': '',
...         'message': 'Hi there',
...         'sender': 'invalid email address',
...         'cc_myself': True}
>>> f = ContactForm(data)
>>> f.is_valid()
False

Form.errors¶

Access the errors attribute to get a dictionary of error messages:

>>> f.errors
{'sender': ['Enter a valid email address.'], 'subject': ['This field is required.']}

In this dictionary, the keys are the field names, and the values are lists of strings representing the error messages. The error messages are stored in lists because a field can have multiple error messages.

You can access errors without having to call is_valid() first. The form’s data will be validated the first time either you call is_valid() or access errors.

The validation routines will only get called once, regardless of how many times you access errors or call is_valid(). This means that if validation has side effects, those side effects will only be triggered once.

Form.errors.as_data()¶

Returns a dict that maps fields to their original ValidationError instances.

>>> f.errors.as_data()
{'sender': [ValidationError(['Enter a valid email address.'])],
'subject': [ValidationError(['This field is required.'])]}

Use this method anytime you need to identify an error by its code. This enables things like rewriting the error’s message or writing custom logic in a view when a given error is present. It can also be used to serialize the errors in a custom format (e.g. XML); for instance, as_json() relies on as_data().

The need for the as_data() method is due to backwards compatibility. Previously ValidationError instances were lost as soon as their rendered error messages were added to the Form.errors dictionary. Ideally Form.errors would have stored ValidationError instances and methods with an as_ prefix could render them, but it had to be done the other way around in order not to break code that expects rendered error messages in Form.errors.

Form.errors.as_json(escape_html=False)¶

Returns the errors serialized as JSON.

>>> f.errors.as_json()
{"sender": [{"message": "Enter a valid email address.", "code": "invalid"}],
"subject": [{"message": "This field is required.", "code": "required"}]}

By default, as_json() does not escape its output. If you are using it for something like AJAX requests to a form view where the client interprets the response and inserts errors into the page, you’ll want to be sure to escape the results on the client-side to avoid the possibility of a cross-site scripting attack. It’s trivial to do so using a JavaScript library like jQuery - simply use $(el).text(errorText) rather than .html().

If for some reason you don’t want to use client-side escaping, you can also set escape_html=True and error messages will be escaped so you can use them directly in HTML.

Form.errors.get_json_data(escape_html=False)¶

Returns the errors as a dictionary suitable for serializing to JSON. Form.errors.as_json() returns serialized JSON, while this returns the error data before it’s serialized.

The escape_html parameter behaves as described in Form.errors.as_json().

Form.add_error(field, error)¶

This method allows adding errors to specific fields from within the Form.clean() method, or from outside the form altogether; for instance from a view.

The field argument is the name of the field to which the errors should be added. If its value is None the error will be treated as a non-field error as returned by Form.non_field_errors().

The error argument can be a simple string, or preferably an instance of ValidationError. See Raising ValidationError for best practices when defining form errors.

Note that Form.add_error() automatically removes the relevant field from cleaned_data.

Form.has_error(field, code=None)¶

This method returns a boolean designating whether a field has an error with a specific error code. If code is None, it will return True if the field contains any errors at all.

To check for non-field errors use NON_FIELD_ERRORS as the field parameter.

Form.non_field_errors()¶

This method returns the list of errors from Form.errors that aren’t associated with a particular field. This includes ValidationErrors that are raised in Form.clean() and errors added using Form.add_error(None, "...").
Behavior of unbound forms¶

It’s meaningless to validate a form with no data, but, for the record, here’s what happens with unbound forms:

>>> f = ContactForm()
>>> f.is_valid()
False
>>> f.errors
{}

Dynamic initial values¶

Form.initial¶

Use initial to declare the initial value of form fields at runtime. For example, you might want to fill in a username field with the username of the current session.

To accomplish this, use the initial argument to a Form. This argument, if given, should be a dictionary mapping field names to initial values. Only include the fields for which you’re specifying an initial value; it’s not necessary to include every field in your form. For example:

>>> f = ContactForm(initial={'subject': 'Hi there!'})

These values are only displayed for unbound forms, and they’re not used as fallback values if a particular value isn’t provided.

If a Field defines initial and you include initial when instantiating the Form, then the latter initial will have precedence. In this example, initial is provided both at the field level and at the form instance level, and the latter gets precedence:

>>> from django import forms
>>> class CommentForm(forms.Form):
...     name = forms.CharField(initial='class')
...     url = forms.URLField()
...     comment = forms.CharField()
>>> f = CommentForm(initial={'name': 'instance'}, auto_id=False)
>>> print(f)
<tr><th>Name:</th><td><input type="text" name="name" value="instance" required></td></tr>
<tr><th>Url:</th><td><input type="url" name="url" required></td></tr>
<tr><th>Comment:</th><td><input type="text" name="comment" required></td></tr>

Form.get_initial_for_field(field, field_name)¶

Use get_initial_for_field() to retrieve initial data for a form field. It retrieves data from Form.initial and Field.initial, in that order, and evaluates any callable initial values.
Checking which form data has changed¶

Form.has_changed()¶

Use the has_changed() method on your Form when you need to check if the form data has been changed from the initial data.

>>> data = {'subject': 'hello',
...         'message': 'Hi there',
...         'sender': 'foo@example.com',
...         'cc_myself': True}
>>> f = ContactForm(data, initial=data)
>>> f.has_changed()
False

When the form is submitted, we reconstruct it and provide the original data so that the comparison can be done:

>>> f = ContactForm(request.POST, initial=data)
>>> f.has_changed()

Form.cleaned_data¶
 >>> data = {'subject': 'hello',
...         'message': 'Hi there',
...         'sender': 'foo@example.com',
...         'cc_myself': True}
>>> f = ContactForm(data)
>>> f.is_valid()
True
>>> f.cleaned_data
{'cc_myself': True, 'message': 'Hi there', 'sender': 'foo@example.com', 'subject': 'hello'}
***