# Generated by Django 2.1.2 on 2018-10-19 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('decut', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='signup_model',
            name='id',
        ),
        migrations.AlterField(
            model_name='signup_model',
            name='emial',
            field=models.EmailField(max_length=254, primary_key=True, serialize=False),
        ),
    ]