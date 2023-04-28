from django.contrib import admin

from .models import Attachment, Category, Product


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'condition', 'price')
    list_filter = ('category',)
    search_fields = ('name', 'category',)


class AttachmentAdmin(admin.ModelAdmin):
    list_display = ('file', 'product')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Attachment, AttachmentAdmin)
