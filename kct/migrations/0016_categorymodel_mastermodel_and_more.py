# Generated by Django 5.1.5 on 2025-01-30 09:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("kct", "0015_managinglistcategorymaster_listitemcategory"),
    ]

    operations = [
        migrations.CreateModel(
            name="CategoryModel",
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
                ("category_name", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="MasterModel",
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
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("beneficiary", "Beneficiary"),
                            ("key_program", "Key Program"),
                            ("event", "Event"),
                            ("case_study", "Case Study"),
                            ("aid", "Aid"),
                        ],
                        max_length=20,
                    ),
                ),
                ("title", models.CharField(max_length=255)),
                ("description", models.TextField(blank=True, null=True)),
                ("count", models.IntegerField(blank=True, null=True)),
                (
                    "image",
                    models.FileField(blank=True, null=True, upload_to="master_images/"),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("active", models.BooleanField(default=True)),
            ],
        ),
        migrations.RenameModel(
            old_name="ListItemCategory",
            new_name="ListItem",
        ),
        migrations.RenameModel(
            old_name="ManagingListCategoryMaster",
            new_name="ManagingListCategory",
        ),
        migrations.DeleteModel(
            name="BeneficiaryAid",
        ),
        migrations.RemoveField(
            model_name="beneficiarycategory",
            name="beneficiary_id",
        ),
        migrations.DeleteModel(
            name="CaseStudiesMaster",
        ),
        migrations.DeleteModel(
            name="KeyProgramMaster",
        ),
        migrations.DeleteModel(
            name="LatestEventMaster",
        ),
        migrations.AddField(
            model_name="categorymodel",
            name="parent",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="categories",
                to="kct.mastermodel",
            ),
        ),
        migrations.DeleteModel(
            name="BeneficiaryCategory",
        ),
        migrations.DeleteModel(
            name="BeneficiaryMaster",
        ),
    ]
