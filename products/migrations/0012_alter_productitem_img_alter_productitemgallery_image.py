# Generated by Django 4.2.3 on 2023-08-01 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0011_alter_productitem_img"),
    ]

    operations = [
        migrations.AlterField(
            model_name="productitem",
            name="img",
            field=models.ImageField(upload_to="productTitle"),
        ),
        migrations.AlterField(
            model_name="productitemgallery",
            name="image",
            field=models.ImageField(upload_to="images"),
        ),
    ]
