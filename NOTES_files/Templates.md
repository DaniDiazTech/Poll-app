# Templates in Django

The Django Templates Language, is a language that allows you to manipulate 
elements of html files. 

It allows you to save time avoiding copy-pasting in a large amount of static  files.

## Elements in DTL

The variables in Django template are set with double curly braces

```html
<p>{{ name_of_variable }}}</p>
```

The flow statements are set like {% flow statement %}, and this kind of statements 
ends with {% end(name of statement)%}:

```html
{% if condition %}
<p>Some text</p>
{% else %}
<p>Other kind of text</p>
{% endif %}
```

For instance the for loop is:

```html
{% for object in iterable_object %}
{% endfor %}
```

## Template structure

To create the templates of an app in Django you need to create two folders. One called **templates**,
and inside that templates folder, other folder with the name of the app.

The tree structure of the app, should be like this:

```vim
├── admin.py
├── apps.py
├── __init__.py
├── migrations
├── models.py
├── templates
│   └── poll
│       ├── base.html
│       ├── detail.html
│       ├── footer.html
│       ├── home.html
│       └── index.html
├── tests.py
├── urls.py
└── views.py
```

But why is it necessary to create a template folder and inside a folder with the name of the app?

Well it is because Django joins all the templates of the installed apps, in a big templates folder.

So for example if we have two files with the same name, in different apps, Django will be confused 
about what file it needs to show.

With  the double named folder structure, that can't happen because each mini template folder has 
the name of it's corresponding app.

## Extending templates

Once you've understand the basic variables and flow statement tags, you will want
to optimize the way you write your templates. Here is where extending templates come handy.

Let' suppose you have a **base.html** file where you have a standard html skeleton, and you
want to write a html for the home page of your site.

You don't want to copy and paste the base.html that you previously create, so you use the Django
Template Language to simplify the task.

With the  `{% extends "base.html" %}`  tag,you can approach the html file that you created.

So if you have a simple skeleton like this:

`base.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
</head>
<body>

</body>
</html>
```

You could implement it in your index page:

`index.html`

```html
{% extends 'base.html' %}
```

With this shortcut, you don't have to paste the basic structure of a html file each time you 
need to create other page.

Ok, but what happens when you want add content to the file you just extended?

For this task the `{% block content %}` tag is the correct choice, let's  see how it works.

`base.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
</head>
<body>
{% block body %}
<p>Original content</p>
{% endblock %}
</body>
</html>
```

`index.html`

```html
{% extends 'base.html' %}

{% block body %}
<p>This paragraph should be added to the body of the skeleton html</p>
{% endblock %}
```

As you see the block tag allows us to write some html tags, in the file we expanded.

But we have a problem, when we write in a `{% block body %}` tag all the things inside the 
original block are override, so the solution is use `{{ block.super }}` variable. It allows
us to append tags inside the blog instead of just override the entire block.

`final_index.html`

```html
{% extends 'base.html' %}

{% block body %}
{{ block.super }}
<p>This paragraph should be added to the body of the skeleton html</p>
{% endblock %}
```

There are several tags in DTL so I encourage you, to review 
the [official documentation](https://docs.djangoproject.com/en/3.1/ref/templates/language/)
 