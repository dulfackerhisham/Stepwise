# Generated by Django 4.2.3 on 2023-08-02 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0013_category_image_alter_productitem_img_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="productitem",
            name="createdDate",
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
