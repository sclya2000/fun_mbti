# Generated by Django 3.0.5 on 2020-05-09 02:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20200509_0216'),
    ]

    operations = [
        migrations.RenameField(
            model_name='note',
            old_name='personality',
            new_name='personality1',
        ),
    ]
