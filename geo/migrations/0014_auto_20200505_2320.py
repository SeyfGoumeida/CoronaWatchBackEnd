# Generated by Django 3.0.4 on 2020-05-05 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geo', '0013_auto_20200401_2003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='regions',
            name='riskregion',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='regions',
            name='riskvalide',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
