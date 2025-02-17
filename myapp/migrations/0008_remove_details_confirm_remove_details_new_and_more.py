# Generated by Django 5.0.4 on 2024-05-28 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_details_remove_registration_last_login'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='details',
            name='confirm',
        ),
        migrations.RemoveField(
            model_name='details',
            name='new',
        ),
        migrations.AddField(
            model_name='details',
            name='password',
            field=models.CharField(blank=True, max_length=128),
        ),
        migrations.AlterField(
            model_name='details',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
    ]
