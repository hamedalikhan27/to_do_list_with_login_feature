# Generated by Django 4.2.3 on 2023-08-22 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('to_do_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addtask',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
