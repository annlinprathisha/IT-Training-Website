# Generated by Django 5.0.4 on 2024-04-27 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_alter_registration_guardians_mobile_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='choose_your_course',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='registration',
            name='gender',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='registration',
            name='location',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='registration',
            name='training_mode',
            field=models.CharField(max_length=20),
        ),
    ]
