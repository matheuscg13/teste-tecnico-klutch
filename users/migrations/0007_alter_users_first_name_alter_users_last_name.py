# Generated by Django 4.2.5 on 2023-10-06 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_users_last_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='first_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='users',
            name='last_name',
            field=models.CharField(max_length=50),
        ),
    ]