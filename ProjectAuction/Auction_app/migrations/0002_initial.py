# Generated by Django 4.0.5 on 2022-06-21 09:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Auction_app', '0001_initial'),
        ('Seller_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userwishlist',
            name='myuser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='securitydeposite',
            name='currentauction',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Auction_app.currentauction'),
        ),
        migrations.AddField(
            model_name='securitydeposite',
            name='myuser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='currentbid',
            name='bidder',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Auction_app.bidder'),
        ),
        migrations.AddField(
            model_name='currentbid',
            name='currentauction',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Auction_app.currentauction'),
        ),
        migrations.AddField(
            model_name='currentauction',
            name='auction_details',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Auction_app.auctiondetails'),
        ),
        migrations.AddField(
            model_name='bidder',
            name='currentauction',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Auction_app.currentauction'),
        ),
        migrations.AddField(
            model_name='bidder',
            name='myuser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='autobid',
            name='bidder',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Auction_app.bidder'),
        ),
        migrations.AddField(
            model_name='auctiondetails',
            name='product_information',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Seller_app.productinformation'),
        ),
        migrations.AddField(
            model_name='allbid',
            name='auctiondetails',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Auction_app.auctiondetails'),
        ),
        migrations.AddField(
            model_name='allbid',
            name='bidder',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
