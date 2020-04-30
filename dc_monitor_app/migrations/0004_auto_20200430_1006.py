# Generated by Django 3.0.5 on 2020-04-30 10:06

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('dc_monitor_app', '0003_auto_20200430_0441'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApplianceCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('Home Products Services', 'Home Products Services'), ('Air Conditioning', 'Air Conditioning'), ('Electronic Pest Control', 'Electronic Pest Control'), ('Home Air Cleaners', 'Home Air Cleaners'), ('Household Cleaning Equipment', 'Household Cleaning Equipment'), ('Laundry Appliances', 'Laundry Appliances'), ('Small Home Appliances', 'Small Home Appliances'), ('Space Heaters', 'Space Heaters'), ('Water Heaters', 'Water Heaters'), ('Cooking Appliances', 'Cooking Appliances'), ('Dishwashers & Dryers', 'Dishwashers & Dryers'), ('Electric Coffee Makers', 'Electric Coffee Makers'), ('Electric Kettles & Boiling Appliances', 'Electric Kettles & Boiling Appliances'), ('Food Preparation Appliances', 'Food Preparation Appliances'), ('Fridges & Freezers', 'Fridges & Freezers'), ('Kitchen Ovens', 'Kitchen Ovens'), ('Kitchen Stoves, Tops & Hoods', 'Kitchen Stoves, Tops & Hoods'), ('Small Kitchen Appliances', 'Small Kitchen Appliances'), ('Water Treatment Appliances', 'Water Treatment Appliances'), ('Others', 'Others')], max_length=40, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Factory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('location', models.CharField(blank=True, max_length=100, null=True)),
                ('number', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='clint',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Appliances',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_category', models.CharField(blank=True, max_length=100, null=True)),
                ('model', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=400)),
                ('price', models.FloatField()),
                ('warranty', models.FloatField(blank=True)),
                ('rate', models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('consumption_label', models.PositiveSmallIntegerField(blank=True, choices=[(1, 'A+++'), (2, 'A++'), (3, 'A+'), (4, 'A'), (5, 'B'), (6, 'C')])),
                ('production_Year', models.PositiveSmallIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1999), django.core.validators.MaxValueValidator(2100)])),
                ('wattage', models.FloatField(blank=True)),
                ('wight', models.FloatField(blank=True)),
                ('height', models.FloatField(blank=True)),
                ('depth', models.FloatField(blank=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('appliance_category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='dc_monitor_app.ApplianceCategory')),
                ('factory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dc_monitor_app.Factory')),
                ('seller', models.ManyToManyField(to='dc_monitor_app.Seller')),
            ],
        ),
    ]
