# Generated by Django 4.0.3 on 2023-06-10 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_categorized_addr2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorized',
            name='addr1',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='categorized',
            name='category',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='categorized',
            name='firstimage',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='categorized',
            name='firstimage2',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='categorized',
            name='tel',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
