# Generated by Django 3.0.5 on 2021-03-25 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gifitglobal', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='password',
            field=models.CharField(max_length=250),
        ),
    ]
