# Generated by Django 4.2.4 on 2023-12-20 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_order_user_alter_order_address_alter_order_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='address',
            field=models.TextField(blank=True, default='', max_length=100),
        ),
    ]
