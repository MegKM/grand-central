# Generated by Django 4.2.4 on 2023-12-20 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0008_alter_order_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='VenuePhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('url', models.CharField(max_length=200)),
            ],
        ),
        migrations.RenameModel(
            old_name='Events',
            new_name='Event',
        ),
        migrations.RenameField(
            model_name='eventphoto',
            old_name='food',
            new_name='event',
        ),
        migrations.AlterField(
            model_name='order',
            name='address',
            field=models.TextField(default='', max_length=100),
        ),
    ]