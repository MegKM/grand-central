# Generated by Django 4.2.4 on 2023-12-17 22:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AddedOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='CoffeeSizeOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='CoffeeStrengthOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='CookOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='FoodMenuItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=500)),
                ('price', models.DecimalField(decimal_places=2, default=1.0, max_digits=10)),
                ('inStock', models.BooleanField(default=True)),
                ('added_option', models.ManyToManyField(blank=True, help_text='Select all that apply', to='main_app.addedoption')),
                ('cook_option', models.ManyToManyField(blank=True, help_text='Select all that apply', to='main_app.cookoption')),
            ],
        ),
        migrations.CreateModel(
            name='GravyOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='HotChocolateOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='MilkOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('total_price', models.FloatField(default=1.0)),
                ('notes', models.TextField(max_length=500)),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='RemoveOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='SauceOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='SideOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='SizeOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='SoftDrinkOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='MenuOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=50)),
                ('item', models.ManyToManyField(to='main_app.foodmenuitem')),
            ],
        ),
        migrations.CreateModel(
            name='LineItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.foodmenuitem')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.order')),
            ],
        ),
        migrations.CreateModel(
            name='FoodPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('url', models.CharField(max_length=200)),
                ('food', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.foodmenuitem')),
            ],
        ),
        migrations.AddField(
            model_name='foodmenuitem',
            name='gravy_option',
            field=models.ManyToManyField(blank=True, help_text='Select all that apply', to='main_app.gravyoption'),
        ),
        migrations.AddField(
            model_name='foodmenuitem',
            name='remove_option',
            field=models.ManyToManyField(blank=True, help_text='Select all that apply', to='main_app.removeoption'),
        ),
        migrations.AddField(
            model_name='foodmenuitem',
            name='sauce_option',
            field=models.ManyToManyField(blank=True, help_text='Select all that apply', to='main_app.sauceoption'),
        ),
        migrations.AddField(
            model_name='foodmenuitem',
            name='side_option',
            field=models.ManyToManyField(blank=True, help_text='Select all that apply', to='main_app.sideoption'),
        ),
        migrations.AddField(
            model_name='foodmenuitem',
            name='size_option',
            field=models.ManyToManyField(blank=True, help_text='Select all that apply', to='main_app.sizeoption'),
        ),
        migrations.CreateModel(
            name='DrinkMenuItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=500)),
                ('price', models.DecimalField(decimal_places=2, default=1.0, max_digits=10)),
                ('inStock', models.BooleanField(default=True)),
                ('inhouse_option', models.BooleanField(default=False)),
                ('coffee_size_option', models.ManyToManyField(blank=True, help_text='Select all that apply', to='main_app.coffeesizeoption')),
                ('coffee_strength_option', models.ManyToManyField(blank=True, help_text='Select all that apply', to='main_app.coffeestrengthoption')),
                ('hot_chocolate_option', models.ManyToManyField(blank=True, help_text='Select all that apply', to='main_app.hotchocolateoption')),
                ('milk_option', models.ManyToManyField(blank=True, help_text='Select all that apply', to='main_app.milkoption')),
                ('soft_drink_option', models.ManyToManyField(blank=True, help_text='Select all that apply', to='main_app.softdrinkoption')),
            ],
        ),
        migrations.CreateModel(
            name='DietaryOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=50)),
                ('item', models.ManyToManyField(to='main_app.foodmenuitem')),
            ],
        ),
    ]
