# Generated by Django 4.2.8 on 2023-12-04 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('who_are_you', models.CharField(max_length=2)),
                ('email', models.EmailField(max_length=254)),
                ('full_name', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=15)),
                ('message', models.TextField()),
            ],
        ),
    ]
