# Generated by Django 3.2.8 on 2021-11-15 15:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_feedback'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feedback',
            old_name='feedback',
            new_name='userfeedback',
        ),
    ]