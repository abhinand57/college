# Generated by Django 4.1.5 on 2023-06-03 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0003_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=250)),
                ('lname', models.CharField(max_length=250)),
                ('adress', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('number', models.IntegerField()),
                ('dob', models.IntegerField()),
                ('age', models.IntegerField()),
            ],
        ),
    ]
