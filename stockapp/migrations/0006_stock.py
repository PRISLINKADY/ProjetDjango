# Generated by Django 4.2.10 on 2024-03-12 07:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stockapp', '0005_delete_stock'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantite', models.IntegerField()),
                ('date', models.DateTimeField(auto_now=True)),
                ('type_mouvement', models.CharField(max_length=50)),
                ('produit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stockapp.produit')),
            ],
        ),
    ]