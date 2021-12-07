# Generated by Django 3.0.5 on 2021-01-23 16:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gems', '0021_delete_attendance'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scan_date', models.DateField(null=True)),
                ('scan_time', models.TimeField(null=True)),
                ('location', models.CharField(max_length=75)),
                ('subject', models.CharField(max_length=75)),
                ('teacher', models.CharField(max_length=25)),
                ('hour', models.CharField(max_length=12)),
                ('day', models.CharField(max_length=12)),
                ('enrollment', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='gems.Enrollment')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gems.Student')),
            ],
            options={
                'verbose_name': 'Student Attendance Record',
                'verbose_name_plural': 'Student Attendance Records',
                'ordering': ('scan_date', 'scan_time'),
            },
        ),
        migrations.AddConstraint(
            model_name='attendance',
            constraint=models.UniqueConstraint(fields=('enrollment', 'scan_date'), name='unique_attendance_record'),
        ),
    ]
