# Generated by Django 2.2.3 on 2019-08-29 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0015_auto_20190829_0914'),
    ]

    operations = [
        migrations.CreateModel(
            name='String',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('use_life', models.CharField(default='', max_length=100)),
            ],
        ),
    ]