from django.contrib import admin

from shop.models import Category, Product


# 카테고리 등록
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug']
    prepopulated_fields = {'slug': ('name', )}

# 등록 방법 1
admin.site.register(Category, CategoryAdmin)

# 등록 방법 2
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug', 'category', 'price', 'stock', 'available_display', 'available_order', 'created', 'updated']
    list_filter = ['available_display', 'available_order', 'created', 'updated', 'category']
    prepopulated_fields = {'slug': ('name', )}
    list_editable = ['price', 'stock', 'available_display', 'available_order']
