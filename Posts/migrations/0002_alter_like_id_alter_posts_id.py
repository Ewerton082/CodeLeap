# Generated by Django 5.2.4 on 2025-07-23 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='posts',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
