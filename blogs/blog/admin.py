from django.contrib import admin
from .models import Post, Category

# 관리자 페이지에 Post를 등록
admin.site.register(Post)

# 카테고리 등록
class CategoryAdmin(admin.ModelAdmin):
    # slug와 name이 동시에 입력됨
    prepopulated_fields = {'slug': ('name', )}  # name은 튜플

admin.site.register(Category, CategoryAdmin)