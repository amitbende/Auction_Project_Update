# Generated by Django 4.0.5 on 2022-06-21 09:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Seller_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='productinformation',
            name='myuser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='productinformation',
            name='product_sub_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Seller_app.productsubcategory'),
        ),
        migrations.AddField(
            model_name='productimages',
            name='product_information',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Seller_app.productinformation'),
        ),
    ]
