# Generated by Django 3.0.5 on 2021-02-18 17:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gems', '0029_auto_20210217_1817'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookcheckout',
            options={'verbose_name': 'Book Checkout Record', 'verbose_name_plural': 'Book Checkout Records'},
        ),
        migrations.AlterModelOptions(
            name='itemcategory',
            options={'verbose_name': 'Item Category', 'verbose_name_plural': 'Item Categories'},
        ),
        migrations.AlterModelOptions(
            name='itemcheckout',
            options={'verbose_name': 'Item Checkout Record', 'verbose_name_plural': 'Item Checkout Records'},
        ),
    ]
