# Generated by Django 4.2.8 on 2023-12-04 18:57

from django.db import migrations, models
import testimonialsApp.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClientTestimonial',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('client_name', models.CharField(max_length=255)),
                ('client_pic', models.ImageField(default=testimonialsApp.models.get_default_startup_pic, upload_to='images/')),
                ('client_type', models.CharField(max_length=255)),
                ('client_designation', models.CharField(max_length=255)),
                ('client_rating', models.PositiveIntegerField()),
                ('client_opinion_heading', models.CharField(max_length=255)),
                ('client_opinion', models.TextField()),
            ],
        ),
    ]