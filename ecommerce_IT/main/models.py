from django.db import models
import uuid
# Create your models here.

class Category(models.Model):
    category = models.CharField(max_length=200,null=True,blank=True)

    def __str__(self) -> str:
        return self.category

class Product(models.Model):
    p_name = models.CharField(max_length=200,null=True,blank=True)
    p_price = models.DecimalField(max_digits=100,null=True,blank=True, decimal_places = 2)
    p_image = models.ImageField(null=True,blank=True)
    p_dec = models.TextField(null=True,blank=True)
    category = models.ForeignKey(Category,default=None, null=True, on_delete=models.PROTECT)
    def __str__(self) -> str:
        return self.p_name

class Client(models.Model):
    c_name = models.CharField(max_length=200,null=True,blank=True)
    c_email = models.EmailField(null=True,blank=True)
    c_phone = models.IntegerField(null=True,blank=True)
    def __str__(self) -> str:
        return self.c_name


class Order(models.Model):
    order_id = models.UUIDField(default=uuid.uuid4, unique=True, db_index=True, editable=False)
    order_final_price = models.DecimalField(null=True,blank=True,max_digits=100, decimal_places= 10)
    order_items = models.TextField(null=True,blank=True)
    client = models.ForeignKey(Client,on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.order_id


    



