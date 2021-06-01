# Generated by Django 2.2.5 on 2021-04-01 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ministry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ministry_name', models.CharField(max_length=100, verbose_name='Ministry Name')),
                ('minister_name', models.CharField(max_length=100, verbose_name='Minister Name')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
            ],
        ),
    ]