# Generated by Django 3.0.3 on 2020-02-24 04:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mds', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MR',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('MR_No', models.CharField(max_length=15)),
                ('MR_Name', models.CharField(max_length=50)),
                ('PJT_Client', models.CharField(max_length=30)),
                ('PJT_No', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mds.Project')),
            ],
        ),
    ]