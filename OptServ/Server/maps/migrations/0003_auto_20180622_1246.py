# Generated by Django 2.0.6 on 2018-06-22 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maps', '0002_auto_20180619_1239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bunker',
            name='id',
            field=models.IntegerField(max_length=100, primary_key=True, serialize=False),
        ),
    ]