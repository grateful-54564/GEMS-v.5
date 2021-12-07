# Generated by Django 3.0.5 on 2021-01-08 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gems', '0017_auto_20201224_1843'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='attendance',
            name='unique_attendance_record',
        ),
        migrations.AddField(
            model_name='attendance',
            name='scan_time',
            field=models.TimeField(null=True),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='scan_date',
            field=models.DateField(null=True),
        ),
        migrations.AddConstraint(
            model_name='attendance',
            constraint=models.UniqueConstraint(fields=('enrollment', 'scan_date'), name='unique_attendance_record'),
        ),
    ]