from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class UserModel(AbstractUser):
    email = models.EmailField(_('email address'), blank=False, unique=True)
    age = models.PositiveIntegerField('age', default=0, )
