# Generated by Django 5.1.1 on 2024-12-15 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0013_alter_fileuploudmodel_image_alter_product_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fileuploudmodel',
            name='image',
        ),
        migrations.AddField(
            model_name='fileuploudmodel',
            name='iimage',
            field=models.ImageField(default='', upload_to='images'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='', upload_to='images'),
        ),
    ]
