# Generated by Django 5.1.5 on 2025-02-04 06:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("kct", "0028_alter_systemmaster_system_img"),
    ]

    operations = [
        migrations.CreateModel(
            name="SystemMasterCategory",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name="systemmaster",
            name="category",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="kct.systemmastercategory",
            ),
        ),
    ]
