from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.db.models.signals import pre_save
from django.dispatch import receiver

import inspect


@receiver(pre_save)
def pre_save_full_clean_handler(sender, instance, *args, **kwargs):
    """ Force all models to call full_clean before save """
    from django.contrib.sessions.models import Session

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

    if sender != Session and allowed_by_whitelist:
        instance.full_clean()
