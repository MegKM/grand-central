# Generated by Django 4.2.4 on 2023-12-20 23:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0013_profile_marketing'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='address',
        ),
        migrations.RemoveField(
            model_name='order',
            name='phone',
        ),
    ]