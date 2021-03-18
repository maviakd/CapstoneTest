# Generated by Django 2.2.16 on 2021-03-17 02:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('fileshare', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='files',
            name='file',
        ),
        migrations.RemoveField(
            model_name='files',
            name='owner',
        ),
        migrations.AddField(
            model_name='files',
            name='doc',
            field=models.FileField(blank=True, null=True, upload_to='files/'),
        ),
        migrations.AddField(
            model_name='files',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='files',
            name='date_posted',
            field=models.DateField(default=django.utils.timezone.now, editable=False),
        ),
    ]
