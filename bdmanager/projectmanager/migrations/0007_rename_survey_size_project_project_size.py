# Generated by Django 4.2.7 on 2023-11-23 20:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projectmanager', '0006_project_survey_size_alter_project_cost'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='survey_size',
            new_name='project_size',
        ),
    ]
