# import logging
from django.contrib.admin import models
from django.contrib.auth import get_user_model
from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver

from .models import Client

# from timeline_logger.models import TimelineLog
# from .logentry import LOG_ACTIONS


# logger = logging.getLogger('user_issues')
User = get_user_model()


@receiver(post_save, sender=User)
def create_client(sender, instance, created, *args, **kwargs):
    try:
        if created and instance.email:
            Client.objects.get_or_create(user=instance)
            print("DONE")
    except:
        # TODO logger note
        # logger.error('profile creation failed')
        print("smth went wrong in signal")
