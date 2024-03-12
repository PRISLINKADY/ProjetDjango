# Generated by Django 4.2.10 on 2024-03-04 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stockapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Produit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference', models.IntegerField()),
                ('designation', models.TextField(max_length=50)),
                ('description', models.TextField(blank=True)),
                ('prix_achat', models.FloatField(default=0.0)),
                ('prix_vente', models.FloatField(default=0.0)),
                ('stock_min', models.IntegerField()),
                ('stock_max', models.IntegerField()),
                ('image', models.ImageField(blank=True, upload_to='images')),
                ('categorie', models.ForeignKey(on_delete=models.Model, to='stockapp.categorie')),
            ],
        ),
    ]