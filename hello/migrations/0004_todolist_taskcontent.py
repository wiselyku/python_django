# Generated by Django 3.1.4 on 2020-12-30 23:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0003_auto_20201223_2137'),
    ]

    operations = [
        migrations.AddField(
            model_name='todolist',
            name='taskContent',
            field=models.TextField(default=False),
        ),
    ]
