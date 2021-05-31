## Get and POST for forms:
GET and POST are the only HTTP methods to use when dealing with forms.
Django’s login form is returned using the POST method, in which the browser bundles up the form data, encodes it for transmission, sends it to the server, and then receives back its response.
GET, by contrast, bundles the submitted data into a string, and uses this to compose a URL. The URL contains the address where the data must be sent, as well as the data keys and values. You can see this in action if you do a search in the Django documentation, which will produce a URL of the form https://docs.djangoproject.com/search/?q=forms&release=1.
GET and POST are typically used for different purposes.
Any request that could be used to change the state of the system - for example, a request that makes changes in the database - should use POST. GET should be used only for requests that do not affect the state of the system.
GET would also be unsuitable for a password form, because the password would appear in the URL, and thus, also in browser history and server logs, all in plain text. Neither would it be suitable for large quantities of data, or for binary data, such as an image. A Web application that uses GET requests for admin forms is a security risk: it can be easy for an attacker to mimic a form’s request to gain access to sensitive parts of the system. POST, coupled with other protections like Django’s CSRF protection offers more control over access.
On the other hand, GET is suitable for things like a web search form, because the URLs that represent a GET request can easily be bookmarked, shared, or resubmitted.
Django’s role in forms



## Forms:
A Form instance has an is_valid() method, which runs validation routines for all its fields. When this method is called, if all fields contain valid data, it will return True and place the form’s data in its cleaned_data attribute.



from django import forms
class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)


from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import NameForm
def get_name(request):
    if request.method == 'POST':
        form = NameForm(request.POST) # bound form
        if form.is_valid():
            # process the data in form.cleaned_data as required
            return HttpResponseRedirect('/thanks/')
    else:
        form = NameForm()   # Unbound Form
    return render(request, 'name.html', {'form': form})



Note that it does not include the <form> tags, or a submit button. We’ll have to provide those ourselves in the template.
<form action="/your-name/" method="post">
    {% csrf_token %}
    {{ form }}
    <input type="submit" value="Submit">
</form>


In a similar way that a model class’s fields map to database fields, a form class’s fields map to HTML form <input> elements. 
A form’s fields are themselves classes; they manage form data and perform validation when a form is submitted. A DateField and a FileField handle very different kinds of data and have to do different things with it.



## Bound and unbound forms
    If it’s bound to a set of data, it’s capable of validating that data and rendering the form as HTML with the data displayed in the HTML.
    If it’s unbound, it cannot do validation (because there’s no data to validate!), but it can still render the blank form as HTML.

1. Unbound Form: when there is no data in the form, To create an unbound Form instance, simply instantiate the class:
>>> f = ContactForm()
>>> f.is_bound
False


2. Bound Form: when data is mapped with form, To bind data to a form, pass the data as a dictionary as the first parameter to your Form class constructor:
>>> f = ContactForm({'subject': 'hello'})
>>> f.is_bound
True


Note that passing an empty dictionary creates a bound form with empty data:

>>> f = ContactForm({})
>>> f.is_bound
True



## Form Validation:
Form validation happens when the data is cleaned. If you want to customize this process, there are various places to make changes, each one serving a different purpose. Three types of cleaning methods are run during form processing. These are normally executed when you call the is_valid() method on a form. There are other things that can also trigger cleaning and validation (accessing the errors attribute or calling full_clean() directly), but normally they won’t be needed.

1. is_valid
2. .error
3. full_clean


Note: 1. These methods are run in the order given above, one field at a time. That is, for each field in the form (in the order they are declared in the form definition), the Field.clean() method (or its override) is run, then clean_<fieldname>(). Finally, once those two methods are run for every field, the Form.clean() method, or its override, is executed whether or not the previous methods have raised errors.

2. The clean() method on a Field subclass is responsible for running to_python(), validate(), and run_validators() in the correct order and propagating their errors. If, at any time, any of the methods raise ValidationError, the validation stops and that error is raised. This method returns the clean data, which is then inserted into the cleaned_data dictionary of the form.

Cleaning methods:
1. Field.clean()
2. clean_field_name()
3. form.clean()

Validation method:
1. to_python():  It coerces(convert) the value to a correct datatype and raises ValidationError if that is not possible
2. validate(): this method on a Field handles field-specific validation that is not suitable for a validator. It takes a value that has been coerced to a correct datatype and raises ValidationError on any error
3. run_validators(): this method on a Field runs all of the field’s validators and aggregates all the errors into a single ValidationError.


## Cleaning a specific field attribute
from django import forms
from django.core.exceptions import ValidationError

class ContactForm(forms.Form):
    def clean_recipients(self):
        data = self.cleaned_data['recipients']
        if "fred@example.com" not in data:
            raise ValidationError("You have forgotten about Fred!")
        # Always return a value to use as the new cleaned data, even if
        # this method didn't change it.
        return data


## Validators: A validator is a callable that takes a value and raises a ValidationError if it doesn’t meet some criteria. Validators can be useful for re-using validation logic between different types of fields.

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_even(value):
    if value % 2 != 0:
        raise ValidationError(
            _('%(value)s is not an even number'),
            params={'value': value},
        )
        
from django.db import models

class MyModel(models.Model):
    even_field = models.IntegerField(validators=[validate_even])



## Cleaning and validating fields that depend on each other
There are two ways to report any errors from this step. Probably the most common method is to display the error at the top of the form. To create such an error, you can raise a ValidationError from the clean() method.
1. display the error at the top of the form:
from django import forms
from django.core.exceptions import ValidationError

class ContactForm(forms.Form):
    def clean(self):
        cleaned_data = super().clean()
        cc_myself = cleaned_data.get("cc_myself")
        subject = cleaned_data.get("subject")

        if cc_myself and subject:
            # Only do something if both fields are valid so far.
            if "help" not in subject:
                raise ValidationError(
                    "Did not send for 'help' in the subject despite "
                    "CC'ing yourself."
                )

2. The second approach for reporting validation errors might involve assigning the error message to one of the fields
from django import forms

class ContactForm(forms.Form):
    # Everything as before.
    ...

    def clean(self):
        cleaned_data = super().clean()
        cc_myself = cleaned_data.get("cc_myself")
        subject = cleaned_data.get("subject")

        if cc_myself and subject and "help" not in subject:
            msg = "Must put 'help' in subject when cc'ing yourself."
            self.add_error('cc_myself', msg)
            self.add_error('subject', msg)


Django provides built-in methods to validate form data automatically. Django forms submit only if it contains CSRF tokens. It uses uses a clean and easy approach to validate data.

1. Form.is_valid(): The primary task of a Form object is to validate data. With a bound Form instance, call the is_valid() method to run validation and return a boolean designating whether the data was valid.

>>> data = {'subject': 'hello',
...         'message': 'Hi there',
...         'sender': 'foo@example.com',
...         'cc_myself': True}
>>> f = ContactForm(data)
>>> f.is_valid()
True

Let's try with some invalid data. In this case, subject is blank (an error, because all fields are required by default) and sender is not a valid email address:
>>> data = {'subject': '',
...         'message': 'Hi there',
...         'sender': 'invalid email address',
...         'cc_myself': True}
>>> f = ContactForm(data)
>>> f.is_valid()
False


2. Form.errors: Access the errors attribute to get a dictionary of error messages:

>>> f.errors
{'sender': ['Enter a valid email address.'], 'subject': ['This field is required.']}


3. Form.clean(): Implement a clean() method on your Form when you must add custom validation for fields that are interdependent. See Cleaning and validating fields that depend on each other for example usage.


Note: 1. You can access errors without having to call is_valid() first. The form’s data will be validated the first time either you call is_valid() or access errors.
    2. The validation routines will only get called once, regardless of how many times you access errors or call is_valid(). This means that if validation has side effects, those side effects will only be triggered once.

4. Form.add_error(field, error): This method allows adding errors to specific fields from within the Form.clean() method, or from outside the form altogether; for instance from a view. The field argument is the name of the field to which the errors should be added. If its value is None the error will be treated as a non-field error as returned by Form.non_field_errors(). The error argument can be a simple string, or preferably an instance of ValidationError. 

Note: 1. Form.add_error() automatically removes the relevant field from cleaned_data.

Note: Behavior of unbound forms : It’s meaningless to validate a form with no data, but, for the record, here’s what happens with unbound forms:

>>> f = ContactForm()
>>> f.is_valid()
False
>>> f.errors
{}


5. Form.cleaned_data:
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




*******************************************
## Examples:
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
