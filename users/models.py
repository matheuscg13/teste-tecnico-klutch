from django.db import models
from django.contrib.auth.models import AbstractUser
from localflavor.br.models import BRCPFField

# Create your models here.


class Users(AbstractUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    cpf = BRCPFField(unique=True)

