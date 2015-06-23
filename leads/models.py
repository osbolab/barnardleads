from django.db import models
from django.utils import timezone


from .phones import format_phone


def get_local_time():
    return timezone.localtime(timezone.now())
