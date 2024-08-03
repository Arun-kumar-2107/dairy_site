from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class add_item(models.Model):
    item_name=models.CharField(max_length=100,primary_key=True)
    Item_quentiy = {
        'Kg' : 'kilogram',
        'g' :  'gram',
        'ml': 'mileliter',
        'L':  'liter',
    }
    quantiy=models.CharField(max_length=2,choices=Item_quentiy)
    price=models.IntegerField()
    weight=models.IntegerField()
    user=models.ForeignKey(User,on_delete=models.SET_NULL, null=True,blank=True)