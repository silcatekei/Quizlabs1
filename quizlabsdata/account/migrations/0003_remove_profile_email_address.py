# Generated by Django 5.0.4 on 2024-05-17 17:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_alter_profile_email_address_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='email_address',
        ),
    ]