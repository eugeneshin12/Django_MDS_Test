# Generated by Django 3.0.3 on 2020-03-11 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mds02', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eqt',
            name='E_No',
            field=models.CharField(max_length=20, verbose_name='EQT_No'),
        ),
    ]
