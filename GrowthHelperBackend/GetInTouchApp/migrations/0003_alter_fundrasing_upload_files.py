# Generated by Django 4.2.8 on 2023-12-04 18:46

import GetInTouchApp.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GetInTouchApp', '0002_fundrasing_alter_contact_who_are_you'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fundrasing',
            name='upload_files',
            field=models.FileField(default=GetInTouchApp.models.get_default_startup_pic, upload_to=''),
        ),
    ]
