# Generated by Django 5.1.1 on 2024-12-15 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0011_fileuploudmodel_remove_product_imageurl_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fileuploudmodel',
            name='image',
            field=models.FileField(upload_to='uplouds'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.FileField(default='', upload_to='uplouds'),
        ),
    ]
