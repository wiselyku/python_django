# Generated by Django 3.1.4 on 2020-12-23 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0002_todolist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolist',
            name='finishedDatetime',
            field=models.DateTimeField(null=True),
        ),
    ]
