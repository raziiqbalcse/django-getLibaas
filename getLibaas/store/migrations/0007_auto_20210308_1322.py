# Generated by Django 3.1.7 on 2021-03-08 07:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_authenticate'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Authenticate',
            new_name='Signup',
        ),
    ]