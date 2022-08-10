# Generated by Django 4.1 on 2022-08-08 09:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Quotes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(max_length=250)),
                ('text', models.TextField()),
                ('link', models.URLField(blank=True, db_index=True, max_length=128, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('link', models.URLField(blank=True, db_index=True, max_length=128, unique=True)),
                ('quote', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reminder.quotes')),
            ],
        ),
    ]
