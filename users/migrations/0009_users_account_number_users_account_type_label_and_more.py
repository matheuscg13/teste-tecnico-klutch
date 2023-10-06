# Generated by Django 4.2.5 on 2023-10-06 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_alter_users_password_alter_users_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='account_number',
            field=models.CharField(default=12345678911123456789, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='users',
            name='account_type_label',
            field=models.CharField(choices=[('Conta corrente', 'Current'), ('Conta poupança', 'Savings')], default='Conta corrente', max_length=255),
        ),
        migrations.AddField(
            model_name='users',
            name='bank_label',
            field=models.CharField(default='nubank', max_length=255),
            preserve_default=False,
        ),
    ]