# Generated by Django 4.1.1 on 2022-09-08 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_remove_assignment_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
