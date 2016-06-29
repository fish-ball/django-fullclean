from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.contrib.sessions.models import Session


@receiver(pre_save)
def pre_save_full_clean_handler(sender, instance, *args, **kwargs):
    """ Force all models to call full_clean before save """
    if sender != Session:
        instance.full_clean()

