# Generated by Django 2.0.6 on 2018-06-22 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maps', '0003_auto_20180622_1246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bunker',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
