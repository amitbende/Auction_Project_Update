from ast import Not
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Country(models.Model):
    country_id = models.AutoField(primary_key=True)
    country_name = models.CharField(max_length=50)
    country_code = models.IntegerField()

    class Meta:
        managed = False

    def __str__(self):
        return str(self.country_name)

class State(models.Model):
    state_id = models.AutoField(primary_key=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    state_name = models.CharField(max_length=50)

    class Meta:
        managed = False

    def __str__(self):
        return str(self.state_name)

class City(models.Model):
    city_id = models.AutoField(primary_key=True)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    city_name = models.CharField(max_length=50)

    class Meta:
        managed = False

    def __str__(self):
        return str(self.city_name)

class Address(models.Model):
    area_id = models.AutoField(primary_key=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    area_name = models.CharField(max_length=200)
    street_name = models.CharField(max_length=150)
    house_no = models.CharField(max_length=50)
    area_pincode = models.CharField(max_length=50)

    class Meta:
        managed = False

    def __str__(self):
        return str(self.area_name)

class MyUser(AbstractUser):
    address = models.ForeignKey(Address, on_delete=models.CASCADE, null=True)
    phone_number = models.BigIntegerField(null=True)
    gender = models.CharField(max_length=20)
    is_verified = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    class Meta:
        managed = False

    def __str__(self):
        return str(self.username)

class IdProof(models.Model):
    myuser = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    idproof_id = models.AutoField(primary_key=True)
    idproof_type = models.CharField(max_length=50)
    idproof_image = models.ImageField(upload_to = 'idphoto/')

    class Meta:
        managed = False

    def __str__(self):
        return str(self.idproof_type)





    

