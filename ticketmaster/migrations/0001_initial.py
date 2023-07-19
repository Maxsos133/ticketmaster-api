# Generated by Django 4.2.3 on 2023-07-19 15:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Venue",
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
                ("name", models.CharField(max_length=100)),
                ("location", models.CharField(max_length=100)),
                ("capacity", models.IntegerField()),
                ("bar", models.BooleanField()),
                ("kitchen", models.BooleanField()),
                ("bathrooms", models.IntegerField(null=True)),
                ("outdoor_space", models.CharField(max_length=200, null=True)),
                ("accessibility", models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Event",
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
                ("name", models.CharField(max_length=100)),
                ("date", models.CharField(max_length=100)),
                ("time", models.CharField(max_length=200)),
                ("performers", models.CharField(max_length=200)),
                ("theme", models.CharField(max_length=200)),
                ("tickets_sold", models.IntegerField(null=True)),
                ("tickets_available", models.IntegerField(null=True)),
                (
                    "venue",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="events",
                        to="ticketmaster.venue",
                    ),
                ),
            ],
        ),
    ]
