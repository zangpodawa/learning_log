# Generated by Django 4.2.7 on 2023-11-11 10:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("learning_logs", "0002_entry"),
    ]

    operations = [
        migrations.AddField(
            model_name="topic",
            name="owner",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="entry",
            name="date_added",
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name="topic",
            name="date_added",
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]