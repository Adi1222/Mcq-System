# Generated by Django 2.2.3 on 2019-08-29 12:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0019_remove_profile_ll_counter'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='lifeline2',
            new_name='counter',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='stack',
        ),
    ]
