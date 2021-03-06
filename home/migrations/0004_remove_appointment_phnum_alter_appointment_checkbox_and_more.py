# Generated by Django 4.0.3 on 2022-03-24 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_appointment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='phnum',
        ),
        migrations.AlterField(
            model_name='appointment',
            name='checkbox',
            field=models.CharField(choices=[('M', 'morning'), ('E', 'evening')], max_length=200),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='mail',
            field=models.CharField(choices=[('M', 'email'), ('P', 'phone')], max_length=128),
        ),
    ]
