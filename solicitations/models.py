from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.exceptions import ValidationError
import re

def validate_month_year_format(value):
    if not re.match(r'^(0[1-9]|1[0-2])/\d{2}$', value):
        raise ValidationError('Formato inválido. Use MM/YY.')
    

class TableChoices(models.TextChoices):
    DEFAULT = "Default"
    PARTNER = "Partner"
class ContractChoices(models.TextChoices):
    MANUAL = "Manual"
    AUTOMATICO = "Automatico"

class Solicitations(models.Model):
    client = models.ForeignKey(
"users.Users", on_delete=models.CASCADE, related_name="solicitations"
)
    
    interest_per_installment = models.IntegerField()
    number_of_installments = models.IntegerField(validators=[MaxValueValidator(limit_value=24)])
    installment_value = models.IntegerField()
    total_value = models.IntegerField()
    comission = models.IntegerField()
    card_number = models.CharField(max_length=16)
    card_cvc = models.CharField(max_length=3)
    card_validity = models.CharField(max_length=5, validators=[validate_month_year_format])
    desired_value = models.IntegerField(validators=[MaxValueValidator(limit_value=10000), MinValueValidator(limit_value=300)])
    table = models.CharField(max_length=20, choices=TableChoices.choices, default=TableChoices.DEFAULT)
    contract = models.CharField(choices=ContractChoices.choices, default=ContractChoices.MANUAL)

