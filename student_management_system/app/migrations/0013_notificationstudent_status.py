# Generated by Django 4.1.5 on 2023-01-09 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_notificationstudent'),
    ]

    operations = [
        migrations.AddField(
            model_name='notificationstudent',
            name='status',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
