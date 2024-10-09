# Generated by Django 5.1.2 on 2024-10-09 12:46

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('location_biens', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='date_reservation',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='reservation',
            name='utilisateur',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='reservations_as_utilisateur', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='locataire',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservations_as_locataire', to=settings.AUTH_USER_MODEL),
        ),
    ]