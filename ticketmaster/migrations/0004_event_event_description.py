# Generated by Django 4.2.3 on 2023-07-20 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ticketmaster", "0003_event_img_url_event_venue_name"),
    ]

    operations = [
        migrations.AddField(
            model_name="event",
            name="event_description",
            field=models.TextField(max_length=100, null=True),
        ),
    ]
