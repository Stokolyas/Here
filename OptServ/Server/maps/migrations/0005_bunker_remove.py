# Generated by Django 2.0.6 on 2018-06-30 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maps', '0004_auto_20180622_1624'),
    ]

    operations = [
        migrations.AddField(
            model_name='bunker',
            name='remove',
            field=models.BooleanField(default=0),
            preserve_default=False,
        ),
    ]
