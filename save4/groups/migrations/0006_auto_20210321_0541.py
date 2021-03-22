# Generated by Django 2.2.16 on 2021-03-21 05:41

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0005_auto_20210321_0539'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mygroup',
            name='creator',
            field=models.ForeignKey(default=django.contrib.auth.models.User, editable=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
