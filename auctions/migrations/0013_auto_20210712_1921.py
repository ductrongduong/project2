# Generated by Django 3.1.6 on 2021-07-13 00:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0012_auto_20210712_1645'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-time']},
        ),
    ]
