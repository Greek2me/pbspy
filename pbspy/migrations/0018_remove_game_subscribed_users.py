# Generated by Django 2.2 on 2020-06-22 21:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pbspy', '0017_auto_20200622_2128'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='subscribed_users',
        ),
    ]
