from django.shortcuts import render,redirect
from django.http.response import HttpResponse,HttpResponseNotFound
from django.urls import reverse
data={
    "telefon":"telefon ürün",
    "bilgisayar":"bilgisayar ürün",
    "elektronik":"elektronik ürün"

}
def index(request):
    return  HttpResponse("merhaba")

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
      return HttpResponse(category_text)
    except:
        return HttpResponseNotFound("yanlış kategori secimi")
