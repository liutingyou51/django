# Generated by Django 3.1 on 2020-08-25 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_example', '0002_newuser_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='newuser',
            name='name',
            field=models.CharField(default=' ', max_length=100),
        ),
    ]