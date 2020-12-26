# Generated by Django 3.1 on 2020-12-26 18:56

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='apartment_number',
            field=models.CharField(blank=True, max_length=10, verbose_name='Apartment Numnber'),
        ),
        migrations.AlterField(
            model_name='address',
            name='country',
            field=django_countries.fields.CountryField(max_length=2),
        ),
        migrations.AlterField(
            model_name='address',
            name='flat_number',
            field=models.CharField(blank=True, max_length=10, verbose_name='Flat Numnber'),
        ),
    ]