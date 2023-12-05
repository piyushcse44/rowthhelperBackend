# Generated by Django 4.2.8 on 2023-12-04 20:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('InvestApp', '0010_alter_startup_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='competitor',
            name='sector',
        ),
        migrations.RemoveField(
            model_name='competitor',
            name='startup',
        ),
        migrations.RemoveField(
            model_name='startup',
            name='sector',
        ),
        migrations.DeleteModel(
            name='CompanyDocument',
        ),
        migrations.DeleteModel(
            name='Competitor',
        ),
        migrations.DeleteModel(
            name='Sector',
        ),
        migrations.DeleteModel(
            name='Startup',
        ),
    ]
