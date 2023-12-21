# Generated by Django 4.2.4 on 2023-12-20 21:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main_app', '0011_alter_event_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='address',
            field=models.TextField(help_text='Required for Delivery only', max_length=100),
        ),
        migrations.AlterField(
            model_name='order',
            name='phone',
            field=models.IntegerField(help_text="Any issues, we'll call"),
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.IntegerField(default=0)),
                ('street_address', models.CharField(blank=True, max_length=50)),
                ('suburb', models.CharField(blank=True, max_length=20)),
                ('postcode', models.CharField(blank=True, max_length=4)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
