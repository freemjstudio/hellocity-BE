# Generated by Django 4.0.3 on 2023-06-10 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_categorized'),
    ]

    operations = [
        migrations.AlterField(
            model_name='barrier_free_hotel',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='categorized',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
