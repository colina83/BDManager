# Generated by Django 4.2.7 on 2023-11-23 21:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projectmanager', '0009_sale_delete_sales'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sale',
            old_name='close_date',
            new_name='sale_date',
        ),
        migrations.RemoveField(
            model_name='sale',
            name='sales_date',
        ),
    ]
