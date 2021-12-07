# Generated by Django 3.0.5 on 2020-11-06 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gems', '0010_auto_20201027_1639'),
    ]

    operations = [
        migrations.CreateModel(
            name='HousingUnit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Institution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
            ],
        ),
    ]
