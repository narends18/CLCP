# Generated by Django 4.1.7 on 2023-03-15 13:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0006_rename_class_classe"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Classe",
            new_name="Class",
        ),
    ]