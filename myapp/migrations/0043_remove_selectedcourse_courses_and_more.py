# Generated by Django 5.0.4 on 2024-06-10 13:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0042_registration_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='selectedcourse',
            name='courses',
        ),
        migrations.RemoveField(
            model_name='selectedcourse',
            name='user',
        ),
        migrations.DeleteModel(
            name='Course',
        ),
        migrations.DeleteModel(
            name='SelectedCourse',
        ),
    ]
