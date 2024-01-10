# Generated by Django 5.0.1 on 2024-01-10 11:43

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Gamer",
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
                ("name", models.CharField(max_length=100, verbose_name="Name")),
                ("age", models.IntegerField(max_length=3, verbose_name="Age")),
                ("email", models.EmailField(max_length=277, verbose_name="Email")),
                (
                    "nationality",
                    models.CharField(max_length=100, verbose_name="Nationality"),
                ),
                ("like", models.IntegerField(max_length=100000, verbose_name="Like")),
                (
                    "dislike",
                    models.IntegerField(max_length=100000, verbose_name="Dislike"),
                ),
                (
                    "playlist",
                    models.CharField(max_length=100000, verbose_name="Playlist"),
                ),
                (
                    "wishlist",
                    models.CharField(max_length=100000, verbose_name="Wishlist"),
                ),
            ],
        ),
    ]
