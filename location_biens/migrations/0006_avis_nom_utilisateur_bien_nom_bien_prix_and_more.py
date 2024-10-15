# Generated by Django 5.1.2 on 2024-10-14 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('location_biens', '0005_avis_date_creation_alter_avis_commentaire_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='avis',
            name='nom_utilisateur',
            field=models.CharField(default='Anonyme', max_length=100),
        ),
        migrations.AddField(
            model_name='bien',
            name='nom',
            field=models.CharField(default='Nom par défaut', max_length=100),
        ),
        migrations.AddField(
            model_name='bien',
            name='prix',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='avis',
            name='commentaire',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='bien',
            name='proprietaire',
            field=models.CharField(max_length=100),
        ),
    ]