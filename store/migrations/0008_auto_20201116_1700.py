# Generated by Django 3.1.3 on 2020-11-16 11:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_auto_20201116_1652'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CustomerModel',
            new_name='Customer',
        ),
    ]