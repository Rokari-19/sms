# Generated by Django 4.2.7 on 2024-01-07 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_workname_classname'),
    ]

    operations = [
        migrations.AddField(
            model_name='workname',
            name='submitted_on',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]