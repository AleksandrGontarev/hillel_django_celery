# Generated by Django 4.1 on 2022-08-10 15:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reminder', '0003_remove_author_link'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='quote',
        ),
        migrations.AddField(
            model_name='quotes',
            name='author',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='reminder.author'),
            preserve_default=False,
        ),
    ]
