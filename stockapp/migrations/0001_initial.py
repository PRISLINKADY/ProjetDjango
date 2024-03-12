# Generated by Django 4.2.10 on 2024-03-02 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='images')),
                ('designation', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True)),
            ],
        ),
    ]
