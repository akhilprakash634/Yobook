# Generated by Django 3.2.7 on 2021-09-29 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20210929_2251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='blog',
            field=models.TextField(blank=True),
        ),
    ]
