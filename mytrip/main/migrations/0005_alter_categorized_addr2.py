# Generated by Django 4.0.3 on 2023-06-10 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_barrier_free_hotel_id_alter_categorized_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorized',
            name='addr2',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
