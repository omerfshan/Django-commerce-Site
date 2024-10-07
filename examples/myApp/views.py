from django.shortcuts import render
from django.http.response import HttpResponse


def index(request):
    return  HttpResponse("merhaba")

def details(request):
    return HttpResponse("details")

def list(request):
    return HttpResponse("list")

def getByCategoryId(request,category):
    return HttpResponse(category)

def getByCategory(request,category):
    category_text=None
    if category=="bilgisayar":
        category_text="bilgisayar ürünleri"
    elif category=="telefon":
        category_text="telefon ürünlerii"
    else:
        category_text="yanlış kategori"
    return HttpResponse(category_text)

