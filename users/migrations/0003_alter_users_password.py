# Generated by Django 4.2.5 on 2023-10-06 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_users_cpf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='password',
            field=models.CharField(max_length=128),
        ),
    ]
