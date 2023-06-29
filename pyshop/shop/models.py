from django.db import models

from django.urls import reverse


#Category 모델
class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, unique=True)
    meta_description = models.TextField(blank=True)
    slug = models.SlugField(max_length=100, db_index=True,
                            unique=True, allow_unicode=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):  #product 페이지 경로
        return reverse('shop:product_in_category', args=[self.slug])


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True, unique=True, allow_unicode=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d/', blank=True)
    description = models.TextField(blank=True)  #제품 상세설명
    meta_description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2) #소수 2째자리까지
    stock = models.PositiveIntegerField() #재고 수량
    available_display = models.BooleanField('Display', default=True)
    available_order = models.BooleanField('Order', default=True)

    created = models.DateTimeField(auto_now_add=True) #상품 등록일
    updated = models.DateTimeField(auto_now=True) #수정일

    class Meta:
        ordering = ['-created', '-updated']
        index_together = [['id', 'slug']] #index 기준으로 혼합 사용

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])