# Generated by Django 4.1.1 on 2022-12-03 04:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("movie", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(model_name="movie", name="image",),
    ]
