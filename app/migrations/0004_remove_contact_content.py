# Generated by Django 5.1.2 on 2024-11-29 10:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_remove_contact_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='content',
        ),
    ]