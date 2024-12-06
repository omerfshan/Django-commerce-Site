
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('index',views.index,name="index"),
     path('list',views.list,name="list_view"),
     path('create',views.create),
    path('<slug:slug>',views.details,name="details"),
    # str intleri str olarak alıyor bu yüzden sıra çok önemli
    path('<int:category_id>',views.getByCategoryId),
    path('<str:categorylink>',views.getByCategory,name="category_get")
   
]