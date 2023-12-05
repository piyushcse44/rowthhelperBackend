# Generated by Django 4.2.8 on 2023-12-04 20:12

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('InvestApp', '0008_remove_startup_sector_alter_startup_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='startup',
            name='sector',
            field=models.ManyToManyField(to='InvestApp.sector'),
        ),
        migrations.AlterField(
            model_name='startup',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False),
        ),
    ]
