# Generated by Django 4.2 on 2023-05-05 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("quiz_result", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="quizuser",
            name="time_end",
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name="quizuser",
            name="time_start",
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
