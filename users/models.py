from django.db import models
from django.contrib.auth.models import AbstractUser
from localflavor.br.models import BRCPFField

# Create your models here.
class AccountChoices(models.TextChoices):
    CURRENT = "Conta corrente"
    SAVINGS = "Conta poupança"


class Users(AbstractUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    cpf = BRCPFField(unique=True)
    bank_label = models.CharField(max_length=255)
    account_type_label = models.CharField(max_length=255, choices=AccountChoices.choices, default=AccountChoices.CURRENT)
    account_number = models.CharField(max_length=20)

