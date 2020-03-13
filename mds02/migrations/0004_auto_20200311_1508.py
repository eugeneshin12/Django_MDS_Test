# Generated by Django 3.0.3 on 2020-03-11 06:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mds02', '0003_auto_20200311_1459'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eqt',
            name='M_No',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mds02.MR', verbose_name='MR_No'),
        ),
        migrations.AlterField(
            model_name='eqt',
            name='P_No',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mds02.PJT', verbose_name='PJT_No'),
        ),
    ]
