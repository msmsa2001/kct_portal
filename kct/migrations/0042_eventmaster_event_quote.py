# Generated by Django 5.0.6 on 2025-02-19 11:57

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("kct", "0041_eventmaster_event_feature_eventmaster_kct_remedy_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="eventmaster",
            name="event_quote",
            field=models.CharField(blank=True, max_length=2550, null=True),
        ),
    ]
