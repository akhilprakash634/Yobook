# Generated by Django 3.2.7 on 2021-09-29 18:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_task_blog'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='blog',
        ),
    ]
