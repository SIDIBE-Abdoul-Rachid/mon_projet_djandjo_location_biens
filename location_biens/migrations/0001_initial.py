# Generated by Django 5.1.2 on 2024-10-09 10:51

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bien',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('prix_par_jour', models.DecimalField(decimal_places=2, max_digits=10)),
                ('disponible', models.BooleanField(default=True)),
                ('date_creation', models.DateTimeField(auto_now_add=True)),
                ('proprietaire', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Avis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
                ('commentaire', models.TextField()),
                ('utilisateur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('bien', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='avis', to='location_biens.bien')),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_debut', models.DateField()),
                ('date_fin', models.DateField()),
                ('montant_total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('confirme', models.BooleanField(default=False)),
                ('bien', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='location_biens.bien')),
                ('locataire', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
