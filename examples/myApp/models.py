from django.db import models
from django.utils.text import slugify
# Create your models here.

class Category(models.Model):
   name=models.CharField(max_length=100)
   
   def __str__(self):
      return self.name

class Address(models.Model):
  street=models.CharField(max_length=100)
  postal_code=models.CharField(max_length=5)
  city=models.CharField(max_length=30)

  def __str__(self):
    return f"{self.street} {self.city} {self.postal_code}"

class Supplier(models.Model):
  company_name=models.CharField(max_length=100)
  address=models.OneToOneField(Address,on_delete=models.CASCADE,null=True)

  def __str__(self):
    return self.company_name
  

class Product(models.Model):
  name=models.CharField(max_length=50)
  price=models.DecimalField(max_digits=8,decimal_places=2)
  description=models.CharField(max_length=200)
  imageUrl=models.CharField(max_length=50)
  isActivate=models.BooleanField(default=False)
  category=models.ManyToManyField(Category)
  supplier=models.ForeignKey(Supplier,on_delete=models.CASCADE,null=True)
  slug=models.SlugField(default="",blank=True,null=False,db_index=True,unique=True)
  
  # def save(self,*args,**kwarg):
  #   self.slug=slugify(self.name)
  #   return super().save(*args,**kwarg)

  def __str__(self):
   return f"name: {self.name} price: {self.price} slug: {self.slug}"
