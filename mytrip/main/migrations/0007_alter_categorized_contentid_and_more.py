# Generated by Django 4.0.3 on 2023-06-10 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_categorized_addr1_alter_categorized_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorized',
            name='contentid',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='categorized',
            name='contenttypeid',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='categorized',
            name='field1',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='categorized',
            name='mapx',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='categorized',
            name='mapy',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='categorized',
            name='zipcode',
            field=models.IntegerField(null=True),
        ),
    ]