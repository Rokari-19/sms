# Generated by Django 4.2.7 on 2024-01-07 21:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_classname'),
    ]

    operations = [
        migrations.AddField(
            model_name='workname',
            name='classname',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='items', to='projects.classname'),
        ),
    ]
