# Generated by Django 4.2.3 on 2023-11-28 21:58

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("projects", "0002_project"),
    ]

    operations = [
        migrations.CreateModel(
            name="CertifyingInstitution",
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
                ("url", models.URLField(max_length=500)),
            ],
        ),
    ]
