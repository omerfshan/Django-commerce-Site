from django.db import models
from django.utils.text import slugify
# Create your models here.
class Product(models.Model):
  name=models.CharField(max_length=50)
  price=models.DecimalField(max_digits=8,decimal_places=2)
  description=models.CharField(max_length=200)
  imageUrl=models.CharField(max_length=50)
  isActivate=models.BooleanField(default=False)
  category=models.CharField(max_length=50, null=True)
  slug=models.SlugField(default="",blank=True,null=False,db_index=True,unique=True)
  
  def save(self,*args,**kwarg):
    self.slug=slugify(self.name)
    return super().save(*args,**kwarg)

  def __str__(self):
   return f"name: {self.name} price: {self.price} slug: {self.slug}"
