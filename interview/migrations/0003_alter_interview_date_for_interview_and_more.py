# Generated by Django 4.2.6 on 2023-10-17 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interview', '0002_remove_interview_is_staff'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interview',
            name='date_for_interview',
            field=models.DateField(default=None),
        ),
        migrations.AlterField(
            model_name='interview',
            name='email',
            field=models.EmailField(default=None, max_length=254),
        ),
    ]