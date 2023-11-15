# Generated by Django 4.2.7 on 2023-11-02 21:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("learning_logs", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Entry",
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
                ("date_added", models.DateTimeField(auto_created=True)),
                ("text", models.TextField()),
                (
                    "topic",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="learning_logs.topic",
                    ),
                ),
            ],
            options={"verbose_name_plural": "entries",},
        ),
    ]