# Generated by Django 4.0.5 on 2022-06-21 09:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Auction_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('payment_id', models.AutoField(primary_key=True, serialize=False)),
                ('payment_status', models.BooleanField()),
                ('payment_from', models.CharField(max_length=100)),
                ('payment_to', models.CharField(max_length=100)),
                ('payment_amt', models.BigIntegerField()),
                ('auctiondetails', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Auction_app.auctiondetails')),
            ],
        ),
    ]
