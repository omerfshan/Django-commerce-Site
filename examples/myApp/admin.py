from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display=("name","price","isActivate","slug",)
    list_display_links=("name","price",)
    readonly_fields=("slug",)
    list_filter=("price","category",)
    list_editable=("isActivate",)
    search_fields=("name","description")


admin.site.register(Product,ProductAdmin)
