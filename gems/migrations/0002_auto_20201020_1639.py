# Generated by Django 3.0.5 on 2020-10-20 16:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gems', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testhistory',
            name='student_name',
        ),
        migrations.RemoveField(
            model_name='testhistory',
            name='test_name',
        ),
        migrations.DeleteModel(
            name='Test',
        ),
        migrations.DeleteModel(
            name='TestHistory',
        ),
    ]
