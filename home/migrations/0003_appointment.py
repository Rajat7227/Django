# Generated by Django 4.0.3 on 2022-03-24 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_rename_contactus_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=128)),
                ('phone', models.CharField(max_length=10)),
                ('email', models.CharField(max_length=50)),
                ('date', models.DateField()),
                ('checkbox', models.CharField(max_length=200)),
                ('mail', models.CharField(choices=[('M', 'Mail'), ('P', 'Phnum')], max_length=128)),
                ('phnum', models.CharField(choices=[('M', 'Mail'), ('P', 'Phnum')], max_length=128)),
            ],
        ),
    ]
