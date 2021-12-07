# Generated by Django 3.0.5 on 2020-12-14 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gems', '0014_auto_20201204_1648'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='enrollment',
            name='unique_enrollment_record',
        ),
        migrations.AddConstraint(
            model_name='enrollment',
            constraint=models.UniqueConstraint(fields=('student', 'day', 'class_timeslot'), name='unique_enrollment_record'),
        ),
    ]