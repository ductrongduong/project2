# Generated by Django 3.1.6 on 2021-07-12 21:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0011_auto_20210712_1643'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='listing',
            options={'ordering': ['-created_at']},
        ),
    ]