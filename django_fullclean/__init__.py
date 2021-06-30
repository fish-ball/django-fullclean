from django.apps import apps as django_apps
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.db.models.signals import pre_save
from django.dispatch import receiver

import inspect


@receiver(pre_save)
def pre_save_full_clean_handler(sender, instance, *args, **kwargs):
    """ Force all models to call full_clean before save """
    session_model = getattr(settings, 'FULLCLEAN_SESSION_MODEL', 'django.contrib.sessions.models.Session')
    session = django_apps.get_model(session_model, require_ready=False)

    whitelist = getattr(settings, 'FULLCLEAN_WHITELIST', [''])

    allowed_by_whitelist = False
    
    for item in whitelist:
        if any([isinstance(item, list), isinstance(item, tuple)]):
            if sender.__module__.startswith(item[0]) and sender.__name__ == item[1]:
                allowed_by_whitelist = True
                break
        else:
            if sender.__module__.startswith(item):
                allowed_by_whitelist = True
                break

    if sender != session and allowed_by_whitelist:
        instance.full_clean()
