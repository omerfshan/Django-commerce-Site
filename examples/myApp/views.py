from django.shortcuts import get_object_or_404, render,redirect
from django.http.response import HttpResponse,HttpResponseNotFound,Http404,HttpResponseRedirect
from django.urls import reverse
from datetime import datetime
from . import models
from decimal import Decimal
from django.db.models import Avg,Max,Min
from .form import formProduct

data={
    "telefon":["samsung s20","Samsung s11"],
    "bilgisayar":["laptop 1","laptop 2"],
    "elektronik":[]

}
def index(request):
    # list_items=""
    product=models.Product.objects.filter(isActivate=True).order_by("price")
    product_count=models.Product.objects.filter(isActivate=True).count()
    product_price=models.Product.objects.filter(isActivate=True).aggregate(Avg("price"),Max("price"),Min("price"))
    # category_list=list(data.keys())
    # for category in category_list:
    #     redirect_path=reverse("category_get",args=[category])
    #     list_items+=f"<li><a href=\"{redirect_path}\">{category}</a></li>"
    

    # html=f"<ul>{list_items}</ul>"
    # return  HttpResponse(html)
    return render(request,"index.html",{
        # "categories":category_list,
        "products":product,
        "now":datetime.now,
        "count":product_count,
        "price":product_price
    })

def details(request,slug):
    # try:
    #  product=models.Product.objects.get(pk=id)
    # except:
    #  raise Http404()
    product=get_object_or_404(models.Product,slug=slug)
    content={
        "product":product
    }
    return render(request,"details.html",content)

def list(request):
    if 'q' in request.GET and request.GET.get('q'):
        q=request.GET['q']
        product=models.Product.objects.filter(name__contains=q).order_by("-price")
        
    else:
        product=models.Product.objects.all().order_by("-price")

   
    content={
    "products":product
    }
     
    return render(request,"list.html",content)

def create(request):
    error = False  # Varsayılan olarak hata yok
    if request.method == "POST":
        form=formProduct(request.POST)
        if form.is_valid():
         p = models.Product(name=form.cleaned_data['product_name'], price=form.cleaned_data['price'], description=form.cleaned_data['description'], imageUrl="1.jpg", slug=form.cleaned_data['slug'])
         p.save()
         return HttpResponseRedirect("list")
   
    #     product_name = request.POST['name']
    #     price = request.POST['price']
    #     description = request.POST['description']
    #     slug = request.POST['slug']
    #     # Ürün adı kontrolü
    #     if product_name == "" or len(product_name) < 10:
    #         error = True
    #     else:
    #         # Yeni ürün kaydı
    #         
    #         return HttpResponseRedirect("list")
    
    form=formProduct()
    return render(request, "create.html", {"error": error,"form":form})
 

def getByCategoryId(request,category_id):
    category_list=list(data.keys())
  
    if category_id>len(category_list):
     return HttpResponseNotFound("yanlış kategori secimi")
    
    category_text=category_list[category_id-1]
    redirect_text=reverse("category_get",args=[category_text])
    
    return redirect(redirect_text)

def getByCategory(request,categorylink):
    # try:
      products=data[categorylink]
      return render(request,"products.html",{
          "category":categorylink,
          "products":products
      })
    # except:
        # return HttpResponseNotFound("yanlış kategori secimi")


