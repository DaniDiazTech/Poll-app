# Working with Urls in Django

In this page I will cover the basics of add urls to our Django poll app project.

## What is a Url ? 


Basically a Url (Uniform Resource Locator) is the mechanism that browsers use 
to retrieve a published resource, in the web.

In our case, we are using the **localhost** to test our Django apps.
The local host refers to the local address of our computer, and it usually found
in the IP **127.0.0.1**. 

This means that when an app is trying to call to **127.0.0.1**
it's referring to the local computer.

## Creating url patterns in Django

There are many ways to set a url pattern using Django framework, if 
you want to delve into the matter, read this [Documentation](https://docs.djangoproject.com/en/3.1/topics/http/urls/)

To set a Url pattern in Django, we can introduce it, directly in the main 
directory of our project by modifying the **urlpatterns** variable in the  **urls.py**
file.

We have three options, the first two are by creating a view 
(A function or a class respectively) in our desired app, and linking it to 
the urlpatterns variable, like this:

* With a function

    ```python
    # We need to import the function
    from poll.views import index

    path('polls/', views.index, name='index')
    ```

* With a class

    ```python
    from poll.views import index
    # Now We import a class
    path('', index.as_view(), name='index')
    # Generally the class that contains the view
    # have  a method as_view()
    ```

But there is a third way, where we define a url in the urls.py in the root of the project, 
**but** we _include_ other url configuration for other app.

For example in our project:

* Mysite/urls.py
  
    ```python
    from django.contrib import admin
    # We import include, to be able to include 
    # Other urlconfig
    from django.urls import path, include

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('polls/', include('poll.urls')),
        # Here we include the urls.py file of the app poll
    ] 
    ```

* polls/urls.py

    ```python
    urlpatterns = [
        # Url: localhost:8000/polls/
        path('', views.index, name="index"),
    ] 
    ```

Here we created a file (**urls.py**) in the poll directory and wrote
a variable urlpatterns where we specified the url for our polls app. 