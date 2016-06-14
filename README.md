# django-fullclean

Django app: forcing the model to call full_clean() method on save.

Due to this question in stackoverflow: <http://stackoverflow.com/q/4441539/2544762>

I make the fixture as a tiny PyPI package, to fix this problem.

## Problem

Default in django, when we call the `save()` method on a model, the `full_clean`
method will not be called, witch is useful in fact.

To enable the `full_clean` on `model.save()`, we can just introduce this app
in `settings.py`, and everything is done.

## Usage

Use the standard pip install:

```
pip install django-fullclean
```

If you have the `requirements.txt` in your project, adding `django-fullclean`
inside:

```
# requirements.txt
# ...
django
django-fullclean
# ...
```

Then, in your django project, add `django_fullclean` inside your `INSTALLED_APPS`
section in `settings.py`, the order do not matter:

```
INSTALLED_APPS = (
    # ...
    'django_fullclean',
    # ...
)
```

So now you can freely implement the `clean` method
[ref](https://docs.djangoproject.com/en/1.9/ref/models/instances/#validating-objects),
checking for incorrect cases then throw ValidationError inside.

So you can got an error when you save the model object when the `clean()`
checking is not pass.

Author: [Alfred Huang](https://www.huangwenchao.com.cn)
Email: [57082212@qq.com](mailto:57082212@qq.com)

