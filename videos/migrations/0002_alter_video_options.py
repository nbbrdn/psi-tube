# Generated by Django 4.2.7 on 2023-11-21 13:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='video',
            options={'ordering': ['added']},
        ),
    ]
