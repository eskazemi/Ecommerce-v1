# Generated by Django 4.2 on 2023-08-13 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_otpcode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otpcode',
            name='phone_number',
            field=models.CharField(max_length=11, unique=True),
        ),
    ]
