# Generated by Django 2.2.6 on 2019-10-24 06:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ('-pk',)},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ('-pk',)},
        ),
    ]
