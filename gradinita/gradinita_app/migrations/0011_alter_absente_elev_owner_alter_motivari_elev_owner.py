# Generated by Django 4.1.5 on 2023-03-12 21:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("gradinita_app", "0010_alter_absente_elev_data_alter_motivari_elev_data"),
    ]

    operations = [
        migrations.AlterField(
            model_name="absente_elev",
            name="owner",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="gradinita_app.kids",
            ),
        ),
        migrations.AlterField(
            model_name="motivari_elev",
            name="owner",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="gradinita_app.kids",
            ),
        ),
    ]
