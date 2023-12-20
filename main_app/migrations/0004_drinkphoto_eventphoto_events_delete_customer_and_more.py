# Generated by Django 4.2.4 on 2023-12-19 23:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_customer'),
    ]

    operations = [
        migrations.CreateModel(
            name='DrinkPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('url', models.CharField(max_length=200)),
                ('drink', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.drinkmenuitem')),
            ],
        ),
        migrations.CreateModel(
            name='EventPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('url', models.CharField(max_length=200)),
                ('food', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.foodmenuitem')),
            ],
        ),
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=500)),
            ],
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
        migrations.AddField(
            model_name='lineitem',
            name='cook_option',
            field=models.ManyToManyField(blank=True, help_text='Select all that apply', to='main_app.cookoption'),
        ),
        migrations.AddField(
            model_name='lineitem',
            name='remove_option',
            field=models.ManyToManyField(blank=True, help_text='Select all that apply', to='main_app.removeoption'),
        ),
        migrations.AddField(
            model_name='lineitem',
            name='sauce_option',
            field=models.ManyToManyField(blank=True, help_text='Select all that apply', to='main_app.sauceoption'),
        ),
        migrations.AddField(
            model_name='lineitem',
            name='side_option',
            field=models.ManyToManyField(blank=True, help_text='Select all that apply', to='main_app.sideoption'),
        ),
        migrations.AddField(
            model_name='lineitem',
            name='size_option',
            field=models.ManyToManyField(blank=True, help_text='Select all that apply', to='main_app.sizeoption'),
        ),
    ]