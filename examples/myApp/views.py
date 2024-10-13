from django.shortcuts import render,redirect
from django.http.response import HttpResponse,HttpResponseNotFound
from django.urls import reverse
data={
    "telefon":"telefon ürün",
    "bilgisayar":"bilgisayar ürün",
    "elektronik":"elektronik ürün"

}
def index(request):
    list_items=""
    category_list=list(data.keys())
    for category in category_list:
        redirect_path=reverse("category_get",args=[category])
        list_items+=f"<li><a href=\"{redirect_path}\">{category}</a></li>"
    
    html=f"<ul>{list_items}</ul>"
    # return  HttpResponse(html)
    return render(request,"myApp/index.html")

def details(request):
    return HttpResponse("details")

def lists(request):
    return HttpResponse("lists")

def getByCategoryId(request,category_id):
    category_list=list(data.keys())
    if category_id>len(category_list):
        return HttpResponseNotFound("yanlış kategori secimi")
    category_text=category_list[category_id-1]
    redirect_text=reverse("category_get",args=[category_text])
    return redirect(redirect_text)

def getByCategory(request,category):
    try:
      category_text=data[category]
      return render(request,"myApp/products.html",{
          "category":category,
          "category_text":category_text
      })
    except:
        return HttpResponseNotFound("yanlış kategori secimi")
