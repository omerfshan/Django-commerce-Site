from django.shortcuts import render,redirect
from django.http.response import HttpResponse,HttpResponseNotFound

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
    redirect_text=category_list[category_id-1]
    return redirect("/products/"+redirect_text)

def getByCategory(request,category):
    try:
      category_text=data[category]
      return HttpResponse(category_text)
    except:
        return HttpResponseNotFound("yanlış kategori secimi")
