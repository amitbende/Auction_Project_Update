# Generated by Django 4.0.5 on 2022-06-21 09:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Auction_app', '0002_initial'),
        ('Reports_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='successreport',
            name='product_owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seller', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='feedback',
            name='myuser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='cancelreport',
            name='auctiondetails',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Auction_app.auctiondetails'),
        ),
        migrations.AddField(
            model_name='auctionquery',
            name='auctiondetails',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Auction_app.auctiondetails'),
        ),
        migrations.AddField(
            model_name='auctionquery',
            name='myuser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
