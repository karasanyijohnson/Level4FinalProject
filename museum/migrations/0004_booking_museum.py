# Generated by Django 3.1.4 on 2021-01-02 03:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('museum', '0003_remove_booking_museum'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='museum',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='museum.museum'),
            preserve_default=False,
        ),
    ]