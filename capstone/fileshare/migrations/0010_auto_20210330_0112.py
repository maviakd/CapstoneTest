# Generated by Django 2.2.16 on 2021-03-30 01:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fileshare', '0009_auto_20210330_0110'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='files',
            options={'permissions': (('can_see', 'Can See Files'), ('can_view', 'Can View Files'), ('can_add', 'Can Add Files'))},
        ),
    ]
