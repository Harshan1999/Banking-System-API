# Generated by Django 3.2.9 on 2022-04-27 19:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_account_client'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='branch',
            options={'verbose_name_plural': 'Branches'},
        ),
        migrations.RemoveField(
            model_name='account',
            name='name',
        ),
    ]
