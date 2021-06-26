# django-fullclean

A Django app which forces models to call `full_clean()` method on save.

This tiny PyPI package was created as a solution to the problem posed 
in this question in stackoverflow: <http://stackoverflow.com/q/4441539/2544762>

## Problem

Calling the `full_clean` method when saving a model instance is incredibly useful, 
but does not always occur by default in Django when we call the `save()` method 
on a model.

To enable the `full_clean` on `model.save()`, we can just introduce this app
in `settings.py`, and everything is done.

## Usage

Use the standard pip install:

```
pip install django-fullclean
```

We recommend adding `django-fullclean` to your project's `requirements.txt`:

```
# requirements.txt
# ...
django
django-fullclean
# ...
```

Then, in your Django project, add `django_fullclean` inside the `INSTALLED_APPS`
section of `settings.py`. It's order placement does not matter:

```
INSTALLED_APPS = (
    # ...
    'django_fullclean',
    # ...
)
```

Now you can freely implement the `clean` method
[ref](https://docs.djangoproject.com/en/1.9/ref/models/instances/#validating-objects),
checking for incorrect cases which then throw `ValidationError`.

Now you will properly get an error when the `clean()` checking does not pass 
during model instance `save()`.

## Session Model

In order to prevent problems, django-fullclean ignores the Session model. If you 
are not using Django's built-in Session model, use the `FULLCLEAN_SESSION_MODEL` 
setting to provide the correct model for django-fullclean to ignore. For instance, 
if you are using the `user_session` package, you would add the following to your 
settings.py file:

    FULLCLEAN_SESSION_MODEL = 'user_sessions.models.Session'

## Advanced Usage

If there are specific apps or models you wish to exclude from processing, use the 
`FULLCLEAN_WHITELIST` setting:

```python
FULLCLEAN_WHITELIST = [
    'events',
    ['shop', 'Cart'],
]
```

In the example above, all models in the `events` app will be whitelisted, as well 
as the `Cart` model in the `shop` app, and `django-fullclean` will not call the 
`full_clean` method.

If you wish to skip `full_clean` processing for just a single chunk of code, but 
keep the `full_clean` functionality the rest of the time, you can temporarily 
disconnect the `pre_save_full_clean_handler` signal:

```python
from django.db.models.signals import pre_save
from django_fullclean import pre_save_full_clean_handler

myobject = MyObject.get(id=1)
myobject.name = "Monty"

pre_save.disconnect(pre_save_full_clean_handler)
myobject.save()
pre_save.connect(pre_save_full_clean_handler)
```

## Author

Author: [Alfred Huang](https://www.huangwenchao.com.cn)
Email: [57082212@qq.com](mailto:57082212@qq.com)
