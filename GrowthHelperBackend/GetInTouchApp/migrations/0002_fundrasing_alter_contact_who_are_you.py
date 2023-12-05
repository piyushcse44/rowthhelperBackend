# Generated by Django 4.2.8 on 2023-12-04 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GetInTouchApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FundRasing',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('company_name', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('about_ur_company', models.TextField()),
                ('upload_files', models.URLField()),
                ('phone', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.AlterField(
            model_name='contact',
            name='who_are_you',
            field=models.CharField(max_length=200),
        ),
    ]