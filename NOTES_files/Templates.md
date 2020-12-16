# Templates in Django

The Django Templates Language, is a language that allows you to manipulate 
elements of html files.It allows you to avoid copy-pasting in large html files.

Please refer to the [official documentation](https://docs.djangoproject.com/en/3.1/ref/templates/language/) Since 
I think it is the best resource to learn the main concepts of DTL.

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
{% for object in iterable_object%}
{% endfor %}
```

