# Generated by Django 3.2.7 on 2021-10-05 17:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_task_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='image',
        ),
    ]
