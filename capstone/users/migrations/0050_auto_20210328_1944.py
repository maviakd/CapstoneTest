# Generated by Django 2.2.16 on 2021-03-28 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0049_auto_20210328_1943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ivk',
            name='iv',
            field=models.TextField(default=b'#|\x86\xf4\n@3&\xfe\xaaLq\xf7&\x88G\xcdN\x1d\x8e\xcbj\x0cN\x9a)\xb1H\xa4\xbaG\x0c'),
        ),
    ]