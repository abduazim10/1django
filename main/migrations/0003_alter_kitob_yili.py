# Generated by Django 5.1.3 on 2024-11-30 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_vazifa_alter_kitob_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kitob',
            name='yili',
            field=models.DateField(auto_now=True),
        ),
    ]
