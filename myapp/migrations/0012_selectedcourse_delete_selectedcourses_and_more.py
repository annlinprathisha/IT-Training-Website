# Generated by Django 5.0.4 on 2024-06-02 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_selectedfruit'),
    ]

    operations = [
        migrations.CreateModel(
            name='SelectedCourse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('duration', models.CharField(max_length=50)),
                ('fees', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='SelectedCourses',
        ),
        migrations.DeleteModel(
            name='SelectedFruit',
        ),
    ]
