from django.shortcuts import render,redirect
from django.http.response import HttpResponse,HttpResponseNotFound
from django.urls import reverse
from datetime import datetime
data={
    "telefon":["samsung s20","Samsung s11"],
    "bilgisayar":["laptop 1","laptop 2"],
    "elektronik":[]

}
def index(request):
    # list_items=""
    category_list=list(data.keys())
    # for category in category_list:
    #     redirect_path=reverse("category_get",args=[category])
    #     list_items+=f"<li><a href=\"{redirect_path}\">{category}</a></li>"
    

    # html=f"<ul>{list_items}</ul>"
    # return  HttpResponse(html)
    return render(request,"index.html",{
        "categories":category_list,
        "now":datetime.now
    })

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

def getByCategory(request,categorylink):
    # try:
      products=data[categorylink]
      return render(request,"products.html",{
          "category":categorylink,
          "products":products
      })
    # except:
        # return HttpResponseNotFound("yanlış kategori secimi")
