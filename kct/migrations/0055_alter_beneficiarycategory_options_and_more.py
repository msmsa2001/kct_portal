# Generated by Django 5.1.6 on 2025-03-17 07:23

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("kct", "0054_alter_beneficiarycategory_options_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="beneficiarycategory",
            options={"ordering": ["id"]},
        ),
        migrations.AlterModelOptions(
            name="dropdownoption",
            options={"ordering": ["id"]},
        ),
        migrations.RemoveField(
            model_name="beneficiarycategory",
            name="order",
        ),
        migrations.RemoveField(
            model_name="dropdownoption",
            name="order",
        ),
    ]
