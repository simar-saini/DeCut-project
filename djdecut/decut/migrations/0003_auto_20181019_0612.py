# Generated by Django 2.1.2 on 2018-10-19 06:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('decut', '0002_auto_20181019_0603'),
    ]

    operations = [
        migrations.RenameField(
            model_name='signup_model',
            old_name='emial',
            new_name='email',
        ),
    ]
