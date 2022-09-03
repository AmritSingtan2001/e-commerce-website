from ast import mod
from statistics import mode, quantiles
from django.db import models



choice =(
    ('kg','Kg'),
    ('darjan','Darjan'),
)
class Product(models.Model):
    product_name = models.CharField(max_length=50)
    image = models.ImageField(max_length=200, upload_to="media/image")
    price = models.DecimalField(max_digits=10, decimal_places= 2)
    descriptions = models.CharField(max_length=200)
    unit = models.CharField(choices=choice, max_length=100, default='Kg')
    totalquantites = models.PositiveIntegerField()



    class Meta:
        ordering = ['-id',]

    def __str__(self) :
        return self.product_name



payment_status = (
    ('unpaid','unpaid'),
    ('paid','paid'),
)
 


class Order(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    phone_number = models.IntegerField()
    order_date = models.DateTimeField()
    otp = models.IntegerField(null=True)
    paymentstatus = models.CharField(choices=payment_status, max_length=100, default='unpaid')
   

    def totalprice(self):
        total_price=0
        for items in self.order.all():
            total_price = total_price + items.total
    
    class Meta:
        ordering = ['name',]
    
    def __str__(self) :
        return self.name

    


order_status = (
    ('pending','pending'),
    ('accepted','accepted'),
    ('on the way','on the way'),
    ('delivery','delivery'),
)
class OrderItems(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order')
    product = models.ForeignKey(Product, on_delete= models.CASCADE, related_name= 'product')
    quantity = models.PositiveIntegerField(default='1')
    orderstatus = models.CharField(choices=order_status, default='pending', max_length=100)

    def total(self):
        total = self.quantity * self.product.price
        return total

    
      


    




