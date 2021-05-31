# Generated by Django 3.1.6 on 2021-05-09 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0082_auto_20210509_2036'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='space',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='profile',
            name='total_download_files',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='profile',
            name='total_given_files',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='profile',
            name='total_groups',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='profile',
            name='total_owned_files',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='profile',
            name='total_uploaded_files',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='ivk',
            name='iv',
            field=models.TextField(default=b'\xf4sp[C\xae\x1b-\xf4\xa2\xaau\x81\xd3\xa7\xe1I\xdaX\xd0\xe7i\xd1\xbb\xe0\xdc\t\x038\x93\xd4\x9a'),
        ),
    ]