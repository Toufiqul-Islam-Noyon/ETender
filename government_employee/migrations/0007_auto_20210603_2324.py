# Generated by Django 3.1.6 on 2021-06-03 17:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('government_employee', '0006_tendernotice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='winnerholder',
            name='username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
