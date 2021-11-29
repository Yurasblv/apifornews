# Generated by Django 3.2.9 on 2021-11-28 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("newsapi", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="news",
            old_name="up_votes",
            new_name="vote",
        ),
        migrations.AlterField(
            model_name="comment",
            name="created",
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.DeleteModel(
            name="UpVote",
        ),
    ]
