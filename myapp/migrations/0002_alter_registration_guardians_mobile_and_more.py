# Generated by Django 5.0.4 on 2024-04-27 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='guardians_mobile',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='registration',
            name='mobile_number',
            field=models.IntegerField(),
        ),
    ]
