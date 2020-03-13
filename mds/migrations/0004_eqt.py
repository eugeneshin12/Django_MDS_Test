# Generated by Django 3.0.3 on 2020-02-24 08:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mds', '0003_remove_mr_pjt_client'),
    ]

    operations = [
        migrations.CreateModel(
            name='EQT',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('EQT_No', models.CharField(max_length=20)),
                ('EQT_Name', models.CharField(max_length=40)),
                ('MR_No', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mds.MR')),
                ('PJT_No', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mds.Project')),
            ],
        ),
    ]