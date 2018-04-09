from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.db.models.signals import pre_save
from django.dispatch import receiver

import inspect


@receiver(pre_save)
def pre_save_full_clean_handler(sender, instance, *args, **kwargs):
    """ Force all models to call full_clean before save """
    from django.contrib.sessions.models import Session

    allowed_by_whitelist = settings.FULLCLEAN_WHITELIST \
            and any([sender.__module__.startswith(s) for s in settings.FULLCLEAN_WHITELIST])

    if sender != Session and allowed_by_whitelist:
        instance.full_clean()
