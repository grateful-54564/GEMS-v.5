# Generated by Django 3.0.5 on 2021-02-23 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gems', '0032_auto_20210218_1800'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='checkout_duration',
            field=models.IntegerField(default=14, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='checkout_duration',
            field=models.IntegerField(default=14, null=True),
        ),
    ]
