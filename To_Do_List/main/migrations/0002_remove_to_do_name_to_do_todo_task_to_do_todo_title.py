# Generated by Django 5.1.4 on 2025-01-08 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="to_do",
            name="name",
        ),
        migrations.AddField(
            model_name="to_do",
            name="todo_task",
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name="to_do",
            name="todo_title",
            field=models.TextField(null=True),
        ),
    ]