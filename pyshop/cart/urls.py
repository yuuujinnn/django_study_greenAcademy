from django.urls import path

from cart import views

app_name = 'cart'

urlpatterns = [
    path('', views.detail, name='detail'), # 장바구니 상세
    path('add/<int:product_id>/', views.add, name='product_add'), #장바구니 제품 추가
    path('remove/<int:product_id>/', views.remove, name='product_remove') #장바구니 제품 삭제

]