# Generated by Django 3.0.5 on 2020-05-09 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_note_personality'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='personality',
            field=models.TextField(),
        ),
    ]