# Generated by Django 4.2.4 on 2023-12-14 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_sideoption_delete_sides'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='foodmenuitem',
            name='hasSidesOptions',
        ),
        migrations.RemoveField(
            model_name='sideoption',
            name='dish',
        ),
        migrations.AddField(
            model_name='foodmenuitem',
            name='side_option',
            field=models.ManyToManyField(to='main_app.sideoption'),
        ),
        migrations.AddField(
            model_name='sideoption',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]
