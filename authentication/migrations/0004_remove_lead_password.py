# Generated by Django 3.0.14 on 2022-03-22 16:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_remark'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lead',
            name='password',
        ),
    ]
